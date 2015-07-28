from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import auth
from django.core.context_processors import csrf
from django.conf import settings
from .forms import SignUpForm, ContactForm, areaForm
# Create your views here.

def search(request):
    print request.POST
    return render(request, "search.html", {})

def check_search(request):
    home_dropdown = request.POST.get('home_dropdown')
    home_search = request.POST.get('home_search')
    print home_dropdown, home_search
    if home_search:
        print "redirect"
        return render(request, "search.html", {})

def home(request):
    context = {}
    if request.user.is_authenticated():
        context = {"full_name": request.user.username}
    check_search(request)
    return render(request, "home.html", context)

def landingPage(request):
    return render(request, "index.html", {})

def about(request):
    context = {"message": "This is about page"}
    return render(request, "about.html", context)

def login(request):
    context = {"message": "This is login page"}
    return render(request, "login.html", context)

def doctor_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/doctor_loggedin')
    context = {}
    context.update(csrf(request))
    return render(request, "doctor_login.html", context)
def doctor_logout(request):
    full_name = request.user.username
    auth.logout(request)
    # don't use full_name tag as we are using it in navbar
    return render(request, "doctor_logout.html", {'name':full_name})
def doctor_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/doctor_loggedin')
    else:
        context = {"message":"Loging failed"}
        return render(request, "doctor_login.html", context)

    return render(request, "doctor_login.html")
    
def doctor_loggedin(request):
    print "I got called"
    context = {'full_name': request.user.username, "message":"test"}
    return render(request, "doctor_logged.html", context)
def contact(request):   
    form = ContactForm(request.POST or None)
    context= {} 
    if request.user.is_authenticated():
        context = {"full_name": request.user.username}

    if request.method == 'POST':
        #form_email = form.cleaned_data.get('email')
        #form_full_name = form.cleaned_data.get('full_name')
        #form_message = form.cleaned_data.get('message')
        ##subject = "Site contact form"
        #from_email = settings.EMAIL_HOST_USER
        #to_email = form_email
        #contact_message = """
        #%s: %s via %s
        #"""%(form_full_name, form_message, from_email)
        #send_mail(subject, contact_message, from_email, [to_email], fail_silently=True)
        context.update({"message":"* Successfully submitted the message"})
    return render(request, "forms.html", context)
