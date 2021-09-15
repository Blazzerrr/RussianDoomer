import time
from doomer.donations import getNewDonations


while True:
    getNewDonations()
    time.sleep(3)
