from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def contact(request);
    return  HttpResponse('contact view')
