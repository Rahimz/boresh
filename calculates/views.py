from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def entry(request):
    time = datetime.datetime.now()
    
    return render(request, 'calculates/entry.html', {'test': time})
