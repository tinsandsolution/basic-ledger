# views.py

from django.shortcuts import render

def index(request):
    # Serve React App app/frontend/index.html
    return render(request, 'index.html')
