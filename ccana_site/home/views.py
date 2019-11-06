from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    template=loader.get_template('home/index.html')
    return render(request, 'home/index.html')
