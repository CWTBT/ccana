from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from home.forms import ContactForm


# Create your views here.
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
    if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
