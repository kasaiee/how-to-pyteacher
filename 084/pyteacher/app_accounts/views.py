from django.shortcuts import render
from app_accounts.models import RegisteredItem
from app_social.models import Bookmark
from django.contrib.auth.decorators import login_required
from app_accounts.forms import ProfileForm
from app_accounts.models import Profile
from app_chat.models import Ticket
from django.core.paginator import Paginator
from django.forms.models import modelform_factory
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def profile(request):
    ctx = {}
    ctx['registered_course'] = [rc.course for rc in request.user.registereditem_set.all()]
    return render(request, 'student-dashboard.html', ctx)


def resume(request, username):
    ctx = {}
    ctx['user'] = User.objects.get(username=username)
    return render(request, 'resume.html')


@login_required
def booked_items(request):
    ctx = {}
    booked_items = Bookmark.objects.filter(user=request.user)
    ctx['items'] = [book_item.content_object for book_item in booked_items]
    return render(request, 'booked-items.html', ctx)


@login_required
def edit_profile(request):
    ctx = {}
    if request.method == 'POST':
        ctx['form'] = form = ProfileForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            ctx['form'] = form
    else:
        ctx['form'] = form = ProfileForm(user=request.user)
    ctx['new_avatar'] = Profile.objects.get(user=request.user).avatar
    return render(request, 'student-profile.html', ctx)


@login_required
def ticket_list(request):
    ctx = {}
    page_num = request.GET.get('page') if request.GET.get('page') else 1
    ctx['tickets'] = tickets = Ticket.objects.filter(user=request.user).order_by('-id')
    p = Paginator(tickets, 10)
    ctx['page_num'] = page_num
    ctx['num_pages'] = p.num_pages
    ctx['page'] = p.page(page_num)
    return render(request, 'ticket-list.html', ctx)


@login_required
def ticket_add(request):
    return render(request, 'ticket-add.html')


@login_required
def ticket_detail(request, id):
    return render(request, 'ticket-detail.html', {'ticket': Ticket.objects.get(id=id)})


@login_required
def registered_items(request):
    ctx = {}
    registered_items = request.user.registereditem_set.all().order_by('-id')
    ctx['registered_items'] = set([i.session.course for i in registered_items if i.session])
    return render(request, 'registered-items.html', ctx)
