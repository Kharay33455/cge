from django.shortcuts import render
from .models import *
from django.middleware.csrf import get_token
from django.http import JsonResponse
import json
import base64
import random
from django.utils.datastructures import MultiValueDictKeyError
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
        chatID = str(data['chatID'])
        name = str(data['name'])
        email = str(data['email'])
        title = str(data['title'])
        if chatID == '':
            if name == '' or email == '':
                return JsonResponse({'status' : 204, 'data': 'Name and Email cannot be blank'})
                # all if well, create chat and alert user of success
            else:
                id = ''
                i = 0
                while i < 10:
                    if i % 2 == 0:
                        id = id + str(random.randint(0,9))
                    else:
                        id = id + chr(random.randint(65, 90))
                    i += 1
                
                newChat = Chat.objects.create(chatId = id, name = name, email = email, title = title)
                message = Message.objects.create(text = 'Leave a message describing your issue. Someone would reply to you as soon as possible', fromSupport = True, chat = newChat)
                _chat = {}
                _chat['title'] = newChat.title
                _chat['id'] = newChat.id
                message_list = []
                message_list.append({'text' : message.text, 'image' : None, 'time': message.created.strftime("%H %M"), 'fromSupport' : message.fromSupport})
                _chat['messages'] = message_list
                return JsonResponse({'data' : _chat, 'status' : 200})
        else:
            try:
                chat = Chat.objects.get(chatId = chatID)
                _chat = {}
                _chat['title'] = chat.title
                _chat['id'] = chat.id
                messages = Message.objects.filter(chat = chat)
                message_list = []
                for _ in messages:
                    if _.image:
                        image = _.image.url
                        #image = _.image.read()
                        #encodedImage = base64.b64encode(image).decode('utf-8')
                    else:
                        #encodedImage = None
                        image = None
                    message_list.append({'text' : _.text, 'image' : image, 'time': _.created.strftime("%H %M"), 'fromSupport' : _.fromSupport})
                _chat['messages'] = message_list
                return JsonResponse({'data' : _chat, 'status' : 200})
            except Chat.DoesNotExist:
                context = {'data':'Chat does not exist.', 'status' : 204}
                return JsonResponse(context)
            


def sanitizeData(request):
    text = str(request.POST['text'])
    if text.strip() == "":
        text = None
    try:
        image = request.FILES['image']
    except MultiValueDictKeyError:
        image = None
    chatId = request.POST['chatId']
    return {'text': text, 'image' : image, 'chatId' : chatId}



def sendNewMessage(request):
    if request.method == 'POST':
        # sanitize data
        sanitizedData = sanitizeData(request)
        # only create message if text or image is available
        if sanitizedData['text'] == None and sanitizedData['image'] == None:
            return JsonResponse({'status':403})
        else:
            chat = Chat.objects.get(id = sanitizedData['chatId'])
            new_message = Message.objects.create(text = sanitizedData['text'] , image = sanitizedData['image'], fromSupport = False, chat = chat)
            if new_message.image:
                image = new_message.image.url
            else:
                image = None
            message = {'text' : new_message.text, 'image' : image, 'time' : new_message.created.strftime("%H:%M"), 'fromSupport' : new_message.fromSupport}
            print(message)
            return JsonResponse({'status' : 200, 'message' : message})