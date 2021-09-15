import os
import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import condition
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from doomer.music import getRandomFile
from doomer.messages import getMessages, appendMessages, getTimeEditedMessages, getLastIdMessages
from doomer.donations import getDonations, getTimeEditedDonations, getLastIdDonations


os.environ["TZ"] = "Europe/Moscow"
time.tzset()

def index(request):
    messages = getMessages()
    donations = getDonations()
    lastIdMessages = getLastIdMessages(messages)
    lastIdDonations = getLastIdDonations()

    data = {'messages': messages, 'lastIdMessages': lastIdMessages, 'donations': donations, 'lastIdDonations': lastIdDonations}

    return render(request, 'doomer/index.html', context=data)


def randomMusic(request):
    randomFile = getRandomFile()

    return JsonResponse(randomFile)


@condition(last_modified_func=getTimeEditedMessages)
@never_cache
def messages(request):
    messagesFile = getMessages()
    
    return JsonResponse(messagesFile, safe=False)


@condition(last_modified_func=getTimeEditedDonations)
@never_cache
def donations(request):
    donationsFile = getDonations()
    
    return JsonResponse(donationsFile, safe=False)


@csrf_exempt
def sendMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        appendMessages(name, message)

        return JsonResponse({'success': 'true'}, status=200)