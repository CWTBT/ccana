from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from home.forms import ContactForm
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import get_template

def index(request):
    return render(request, 'home/index.html')

def parents(request):
    return render(request, 'home/parents.html')

def providers(request):
    return render(request, 'home/providers.html')

def staff(request):
    return render(request, 'home/staff.html')

def sponsors(request):
    return render(request, 'home/sponsors.html')

def referral(request):
    return render(request, 'home/referral.html')

def contact(request):
    form_class = ContactForm
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
                contact_name = request.POST.get(
                    'contact_name'
                , '')
                contact_email = request.POST.get(
                    'contact_email'
                , '')
                form_content = request.POST.get('content', '')

                template = get_template('home/contact_template.txt')
                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                }
                content = template.render(context)

                email = EmailMessage(
                    "New contact form submission",
                    content,
                    "CCANA" +'',
                    ['pintered@hendrix.edu'],
                    headers = {'Reply-To': contact_email },
                )
                print("sending to")
                email.send()
                return HttpResponseRedirect('contact_us')

    return render(request, 'home/contact_us.html', {
        'form': form_class,
    })
