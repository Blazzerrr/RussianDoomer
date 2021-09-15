import datetime
from django.db import models


class Messages(models.Model):
	name = models.CharField(max_length=32)
	datetime = models.CharField(max_length=64)
	message = models.CharField(max_length=300)

	def __str__(self):
		return self.datetime


class Donations(models.Model):
	donateId = models.CharField(max_length=16)
	datetime = models.CharField(max_length=64)
	username = models.CharField(max_length=64)
	message = models.CharField(max_length=300)
	amount = models.CharField(max_length=32)
	currency = models.CharField(max_length=16)

	def __str__(self):
		return self.donateId

