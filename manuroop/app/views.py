from django.shortcuts import render,redirect
from .forms import RegForm,Login,ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

# Create your views here.
# @login_required
def home(request):
    return render(request, 'home.html')


# def regform(request):
#    if request.method == 'POST':
#        form = RegForm(request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Registration successful.Please enter username and password!')
#            return redirect('login1')
#    else:
#        form = RegForm()
#    return render(request, 'regform.html', {'form': form})

# def login1(request):
#    if request.method == 'POST':
#        form = Login(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=raw_password)
#            login(request, user)
#            return redirect('home')
#    else:
#        form = Login()
#    return render(request,'login.html',{'form': form})


#def index(request):
#    return render(request,'index.html')

# @login_required
def courses(request):
       return render(request, 'courses.html')
# @login_required
def about(request):
       return render(request, 'about.html')
# @login_required
def partners(request):
       return render(request, 'partner.html')
# @login_required
def leadsquared(request):
       return render(request, 'leadsquared.html')
# @login_required
def microsoftdynamics(request):
       return render(request, 'microsoftdynamics.html')
# @login_required
def pharma(request):
       return render(request, 'pharma.html')
# @login_required
def hospitality(request):
       return render(request, 'hospitality.html')
# @login_required
def real(request):
       return render(request, 'real.html')
# @login_required
def manufacturing(request):
        return render(request, 'manufacture.html')
# @login_required
def agri(request):
        return render(request, 'agri.html')
# @login_required
def ites(request):
        return render(request, 'ites.html')
# @login_required
def nonprofits(request):
        return render(request, 'nonprofit.html')


# @login_required
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            phone = form.cleaned_data.get('phone_number')
            company = form.cleaned_data.get('Company')
            message = form.cleaned_data.get('Message')
            body = {'Name':name,'Email':email,'phone_number':phone,'Company':company,'Message':message},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})

