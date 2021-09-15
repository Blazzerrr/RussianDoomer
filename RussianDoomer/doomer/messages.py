import json
import datetime
from .models import Messages


def getMessages():
	messages = Messages.objects.all().order_by('-id')[:50]
	messagesJson = json.dumps([{'id': m.id, 'name': m.name, 'datetime': m.datetime, 'message': m.message} for m in messages])
	messagesJson = json.loads(messagesJson)
	messagesJson.reverse()

	return messagesJson


def appendMessages(name, message):
	dateNow = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
	m = Messages(name=name, message=message, datetime=dateNow)
	m.save()


def getTimeEditedMessages(request):
	messagesFile = getMessages()
	lastMessage = messagesFile[-1]
	timeEdited = lastMessage['datetime']
	timeEdited = datetime.datetime.strptime(timeEdited, "%d.%m.%Y %H:%M:%S")
	
	return timeEdited


def getLastIdMessages(messages):
	try:
		lastMessage = messages[-1]
		lastId = lastMessage['id']		
	except:
		lastId = '0'

	return lastId


