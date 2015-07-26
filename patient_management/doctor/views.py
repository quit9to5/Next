from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, ContactForm, areaForm
# Create your views here.

def home(request):
    title = "Welcome"
    form = areaForm(request.POST or None)
    context = {
            "template_title": title,
            "form": form
            }
    if form.is_valid():
#
#        instance = form.save(commit=False)
         area = form.cleaned_data.get('full_name')
#        if not full_name:
#            full_name = "New Name"
#        instance.full_name = full_name
#        instance.save()
#        print instance.email
#        print instance.timestamp
#         context = {"template_title": "Thank You"}

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
