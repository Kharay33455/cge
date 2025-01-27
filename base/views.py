from django.shortcuts import render
from .models import *

# Create your views here.

company_name = Company.objects.first()
"""
    Home view
"""
def base(request):
    services = Service.objects.all()

    context = {'services' : services,'company':company_name}
    return render(request, 'base/index.html', context)

def service(request, service_id):
    service = Service.objects.get(id = service_id)
    context = {'service':service, 'company' : company_name}
    return render(request, 'base/service.html', context)
