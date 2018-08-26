from django.shortcuts import render

# Create your views here.

def entry(request):
    return render(request, 'calculates/entry.html', {'test': 'test'})
    

