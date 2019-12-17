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
                    ['test@test.com'],
                    headers = {'Reply-To': contact_email },
                )
                email.send()
                return HttpResponseRedirect('contact_us')

    return render(request, 'home/contact_us.html', {
        'form': form_class,
    })

def referral(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral_name = request.POST.get('referral_name', '')
            referral_email = request.POST.get('referral_email', '')
            from_time = request.POST.get('from_time', '')
            to_time = request.POST.get('to_time', '')
            type = request.POST.get('type', '')
            days = request.POST.get('days', '')
            first_date = request.POST.get('first_date', '')
            second_date = request.POST.get('second_date', '')
            third_date = request.POST.get('third_date', '')
            employer = request.POST.get('employer', '')
            spouse_employer = request.POST.get('spouse_employer', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip = request.POST.get('zip', '')
            county = request.POST.get('county', '')
            phone = request.POST.get('phone', '')

            template = get_template('home/referral_template.txt')
            context = {
                'referral_name': referral_name,
                'referral_email': referral_email,
                'from_time': from_time,
                'to_time': to_time,
                'type': type,
                'days': days,
                'first_date': first_date,
                'second_date': second_date,
                'third_date': third_date,
                'employer': employer,
                'spouse_employer': spouse_employer,
                'address': address,
                'city': city,
                'state': state,
                'zip': zip,
                'county': county,
                'phone': phone,
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
    else:
        print("oops")
        form = ReferralForm()

    return render(request, 'home/referral.html', {
    'form': form
    })
