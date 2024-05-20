from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from cart.forms import AddProductForm
from .forms import *
from .models import *
from .forms import SupportForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate

def index(request):
    kategs=Kategor.objects.all()
    tovar=Tovar.objects.order_by('-price')[:3]
    stat=Stat.objects.all()
    img=Imgtovar.objects.all()
    data={
        'kateg':kategs,
        'stat':stat,
        'tovar':tovar,
        'img':img,
    }
    form = SupportForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'index.html',data)
def katalog(request):
    kateg = Kategor.objects.all()
    data = {
        'kateg': kateg,
    }
    return render(request,'katalog.html',data)
def kateg(request,id):
    kateg = Kategor.objects.all()
    tovar = Tovar.objects.filter(keteg=id)
    stat = Stat.objects.all()
    data={
        'kateg':kateg,
        'stat':stat,
        'tovar':tovar,
    }
    return render(request,'vivod_katalog.html',data)

def filter(request,stat_id):
    kateg = Kategor.objects.all()
    stat = Stat.objects.get(pk=stat_id)
    tovar = Tovar.objects.filter(stat=stat)
    img = Imgtovar.objects.all()
    data={
        'img':img,
        'kateg':kateg,
        'stat':stat,
        'tovar':tovar,
    }
    return render(request,'filter.html',data)

def inform(request,pk):
    kategs = Kategor.objects.all()
    tovar = Tovar.objects.filter(id=pk)
    stat = Stat.objects.all()
    pod_kat=Pod_kat.objects.all()
    tovar1=Tovar.objects.filter(pod_kat=pk)
    kom = Tovar.objects.get(id=pk)
    id_my=pk

    data = {
        'kateg': kategs,
        'stat': stat,
        'pod_kat':pod_kat,
        'tovar': tovar,
        'tovar1': tovar1,
        'tov':kom,
        'pk':id_my,
    }
    if request.method == 'POST':
        form = ModalKom(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.tov = kom
            form.user=request.user
            form.save()
            return redirect('inform', pk=pk)
    return render(request, 'inf.html', data)

def new(request):
    new=New.objects.all()
    data={
        'new':new,
    }
    return render(request,'new.html',data)
def sarch(request):
    kategs = Kategor.objects.all()
    stat = Stat.objects.all()
    img = Imgtovar.objects.all()
    query = request.GET.get('query', None)
    results = []
    if query:
        search_terms = query.split()
        for i in search_terms:
            tovar = Tovar.objects.filter(
                Q(name__icontains=i)| Q(comp__name_company__icontains=i)
            )
            results.extend(tovar)
    data = {
        'kateg': kategs,
        'stat': stat,
        'tovar': tovar,
        'img': img,
    }
    return render(request,'poisk.html',data)

def reg(request):

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            user =form.save()
            messages.success(request, 'Создан аккаунт!')
            return redirect('glavn')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    extra_context = {'title':'Вход'}
def logout_view(request):
    logout(request)
    return redirect('glavn')



@login_required
def prof(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            if profile:
                profile.image = form.cleaned_data['image']
                profile.save()
            else:
                new_profile = Profile(user=request.user, image=form.cleaned_data['image'])
                new_profile.save()
            return redirect('glavn')
    else:
        form = AvatarForm()
    return render(request, 'profil.html', {'user': request.user,'form': form})

def detail(request,id,slug):
    cart_form = AddProductForm()
    tovar = get_object_or_404(Tovar, id=id, slug=slug, available=True)
    return render(request,'index.html',{'tovar':tovar,'cart_form':cart_form})

def about(request):
    return render(request,'about_us.html')
def politik(request):
    return render(request,'politik.html')

def servis(request):
    return render(request,'servis.html')


def social(request):
    return render(request,'social.html')


