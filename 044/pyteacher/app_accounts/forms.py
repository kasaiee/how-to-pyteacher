from django import forms
from django.forms import ModelForm
from app_accounts.models import Profile
from jdatetime import datetime

now = datetime.now()

YEARS = [(i, i) for i in range(1330, now.year + 1)]

MONTHS = list(enumerate(now.j_months_fa))

DAYS = [(day, day) for day in range(1, 32)]


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    username = forms.CharField(label='نام کاربری یا username', max_length=50)
    phone = forms.CharField(label='شماره همراه', max_length=50)
    first_name = forms.CharField(label='نام', max_length=50, required=False)
    last_name = forms.CharField(label='نام خانوادگی', max_length=50, required=False)
    year = forms.ChoiceField(label='سال', choices=YEARS, required=False)
    month = forms.ChoiceField(label='ماه', choices=MONTHS, required=False)
    day = forms.ChoiceField(label='روز', choices=DAYS, required=False)

    def save(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.user)
        profile.bio = self.cleaned_data.get('bio')
        profile.phone = self.cleaned_data.get('phone')
        profile.user.first_name = self.cleaned_data.get('first_name')
        profile.user.last_name = self.cleaned_data.get('last_name')
        profile.user.username = self.cleaned_data.get('username')
        profile.user.save()

    class Meta:
        model = Profile
        exclude = ('user', )
