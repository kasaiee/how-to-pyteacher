from django import forms
from django.forms import ModelForm
from app_accounts.models import Profile
from jdatetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.helper import FormHelper
User = get_user_model()

now = datetime.now()

YEARS = [('', '---')] + [(i, i) for i in range(now.year, 1329, -1)]

MONTHS = [('', '---')] + [(i + 1, j) for i, j in enumerate(now.j_months_fa)]

DAYS = [('', '---')] + [(day, day) for day in range(1, 32)]


def check_phone_num(value):
    if not value.isdigit():
        raise ValidationError('لطفا یه شماره موبایل معتبر وارد کن!')


def check_phone_num_len(value):
    if not (11 <= len(value) <= 13):
        raise ValidationError('طول شماره مبایل نامعتبر است!')


def check_year(value):
    if int(value) > now.year:
        raise ValidationError('لطفا یه سال معتبر وارد کن!')


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='input-field col m4 s12 right'),
                Column('phone', css_class='input-field col m4 s12 right'),
                Column('email', css_class='input-field col m4 s12 right'),
                css_class='row rtl'
            ),
            Row(
                Column('first_name', css_class='input-field col m6 s12 right'),
                Column('last_name', css_class='input-field col m6 s12 right'),
                css_class='row'
            ),
            Row(
                Column('_education', css_class='input-field col m6 s12 right'),
                Column('bio', css_class='input-field col m6 s12 right'),
                css_class='row'
            ),
            Row(
                Column('day', css_class='input-field col m4 s12 right'),
                Column('month', css_class='input-field col m4 s12 right'),
                Column('year', css_class='input-field col m4 s12 right'),
                css_class='row'
            ),
            Submit('submit', 'ثبت')
        )

    username = forms.CharField(label='نام کاربری یا username', max_length=50)
    email = forms.EmailField(label='ایمیل', disabled=True, required=False)
    phone = forms.CharField(label='شماره همراه', max_length=50, required=False, validators=[check_phone_num, check_phone_num_len])
    last_name = forms.CharField(label='نام خانوادگی', max_length=50, required=False)
    first_name = forms.CharField(label='نام', max_length=50, required=False)
    year = forms.ChoiceField(label='سال', choices=YEARS, required=False, validators=[check_year])
    month = forms.ChoiceField(label='ماه', choices=MONTHS, required=False)
    day = forms.ChoiceField(label='روز', choices=DAYS, required=False)

    def clean(self, *args, **kwargs):
        year = int(self.data.get('year')) if self.data.get('year') else None
        month = int(self.data.get('month')) if self.data.get('month') else None
        day = int(self.data.get('day')) if self.data.get('day') else None
        try:
            bd = datetime(year=year, month=month, day=day)
            self.cleaned_data['birth_date'] = bd
        except ValueError:
            self.errors.update({'year': ['لطفا یه تاریخ معتبر وارد کن!']})
        if User.objects.filter(username=self.data.get('username')).exclude(username=self.user.username):
            self.errors.update({'username': ['این نام کاربری قبلا توسط شخص دیگری گرفته شده!']})
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.user)
        profile._education = self.cleaned_data.get('_education')
        profile.bio = self.cleaned_data.get('bio')
        profile.jbirth_date = self.cleaned_data.get('birth_date')
        profile.phone = self.cleaned_data.get('phone')
        profile.user.first_name = self.cleaned_data.get('first_name')
        profile.user.last_name = self.cleaned_data.get('last_name')
        profile.user.username = self.cleaned_data.get('username')
        profile.user.save()

    class Meta:
        model = Profile
        exclude = ('user', 'birth_date')
