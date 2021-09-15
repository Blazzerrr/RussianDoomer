import datetime
import requests
import time
import json
from .models import Donations


TOKEN = "{{DONATIONS_API_KEY}}"


def getDonations():
	donations = Donations.objects.all().order_by('-donateId')[:10]
	donationsJson = json.dumps([{'donateId': d.donateId, 'datetime': d.datetime, 'username': d.username, 'message': d.message, 'amount': d.amount, 'currency': d.currency} for d in donations])
	donationsJson = json.loads(donationsJson)

	return donationsJson


def getLastIdDonations():
    donations = getDonations()
    try:
        lastDonate = donations[0]
    except:
        return '0'

    lastId = lastDonate['donateId']

    return lastId


def addDonate(donateId, username, message, amount, currency):
    dateNow = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    d = Donations(donateId=donateId, datetime=dateNow, username=username, message=message, amount=amount, currency=currency)
    d.save()


def getTimeEditedDonations(request):
    donations = getDonations()

    try:
        lastDonation = donations[0]
    except:
        return '0'

    timeEdited = lastDonation['datetime']
    timeEdited = datetime.datetime.strptime(timeEdited, "%d.%m.%Y %H:%M:%S")

    return timeEdited


def getNewDonations():
    timestamp = time.time()
    timestamp = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(timestamp))

    headers = {"Authorization": f"Bearer {TOKEN}", "If-Modified-Since": timestamp, "Cache-Control": "no-cache"} 

    try:
        res = requests.get('https://www.donationalerts.com/api/v1/alerts/donations', headers=headers, timeout=1) 
    except:
        getNewDonations()
        return

    r = res.json()
    data = r['data'][-10:]

    lastIdNewDonation = data[-1]['id']
    lastIdDonation = getLastIdDonations()

    if lastIdDonation != lastIdNewDonation:
        for donate in data:
            donateId = donate['id']
            if int(donateId) > int(lastIdDonation):
                username = donate['username']
                message = donate['message']
                amount = donate['amount']
                currency = donate['currency']

                addDonate(donateId, username, message, amount, currency)



