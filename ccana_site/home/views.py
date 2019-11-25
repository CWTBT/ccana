from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from collection.forms import ContactForm


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

    return render(request, 'contact.html', {
        'form': form_class,
    })
