

# Create your views here.
from django.shortcuts import render

def contact(request):
    return render(request, 'app2/contact.html')
