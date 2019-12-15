from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from home.forms import ContactForm, ReferralForm
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

def referral(request):
    form_class = ReferralForm
    if request.method == "POST":
       form = ReferralForm(request.POST)
       if form.is_valid():
                contact_name = request.POST.get(
                    'referral_name'
                , '')
                contact_email = request.POST.get(
                    'referral_email'
                , '')
                from_time = request.POST.get(
                    'from_time'
                , '')
                to_time = request.POST.get(
                    'to_time'
                , '')
                needed_days = request.POST.get(
                    'needed_days'
                , '')
                form_content = request.POST.get(
                    'form_content'
                , '')

                template = get_template('home/referral_template.txt')
                context = {
                    'referral_name': contact_name,
                    'referral_email': contact_email,
                    'from_time': from_time,
                    'to_time': to_time,
                    'needed_days': needed_days,
                    'form_content': form_content,
                }
                content = template.render(context)

                email = EmailMessage(
                    "New referral form submission",
                    content,
                    "CCANA" +'',
                    ['pintered@hendrix.edu'],
                    headers = {'Reply-To': referral_email },
                )
                print("sending to")
                email.send()
                return HttpResponseRedirect('referral')

    return render(request, 'home/referral.html', {
        'form': form_class,
    })
