from django.shortcuts import render
from .models import *
from django.middleware.csrf import get_token
from django.http import JsonResponse
import json
# Create your views here.

"""
    Home view
"""
def base(request):
    services = Service.objects.all()
    company= Company.objects.first()
    context = {'services' : services,'company':company}
    return render(request, 'base/index.html', context)

def service(request, service_id):
    service = Service.objects.get(id = service_id)
    company = Company.objects.first()
    _service_headers = ServiceHeader.objects.filter(service = service)
    service_headers = []
    counter = 2
    for _ in _service_headers:

        if counter % 2 == 0:
            right = True
        else:
            right = False
        service_headers.append({'serviceHeader' : _, 'right': right})
        counter += 1
    inner_links = InnerLink.objects.filter(service = service)
    print(service_headers)
    context = {'service':service, 'company' : company, 'serviceHeader': service_headers, 'innerLinks' : inner_links}
    return render(request, 'base/service.html', context)

def payment(request):
    company = Company.objects.first()
    context = {'company' : company}
    return render(request, 'base/payment.html', context)


def chat(request):
    #try:
        #chat = Chat.objects.filter()
    if request.method == 'POST':
        data =  json.loads(request.body)
        # sanitize data
        chatID = data['chatID']
        name = data['name']
        email = data['email']
        try:
            chat = Chat.objects.get(chatId = chatID)
            return JsonResponse({'data' : chat})
        except Chat.DoesNotExist:
            context = {'data':'Chat does not exist.'}
            return JsonResponse(context)