from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
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
    print request.POST
    context = {}
    check_search(request)
    return render(request, "home.html", context)

def landingPage(request):
    return render(request, "index.html", {})

def contact(request):   
    form = ContactForm(request.POST or None)

    context = {
            "form": form
            }
    if form.is_valid():
        print form.cleaned_data
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = form_email
        contact_message = """
        %s: %s via %s
        """%(form_full_name, form_message, from_email)
        send_mail(subject, contact_message, from_email, [to_email], fail_silently=True)
    return render(request, "forms.html", context)
