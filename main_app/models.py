from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from fontawesome_5.fields import IconField
# Create your models here.

class Category(models.Model):
	icon = IconField()

class Friend(models.Model):
	name = models.CharField(max_length=100)
	relationship = models.CharField(max_length=100)
<<<<<<< HEAD
	birthdate = models.DateField()

	user = models.ForeignKey(User, on_delete=models.CASCADE)  
=======
	birthdate = models.DateField()  
>>>>>>> b899c910db1dccdc3530e609fa3e751b1680e069
	
	def __str__(self):
		return self.name

<<<<<<< HEAD
	def get_absolute_url(self):
		return reverse('friends_detail', kwargs={'friend_id': self.id})
=======
>>>>>>> b899c910db1dccdc3530e609fa3e751b1680e069

class Trip(models.Model):
	destination = models.CharField(max_length=100)
	depart = models.DateField('departure date')
	arrive = models.DateField('arrival date')
	hotel = models.CharField(max_length=100)
	budget = models.IntegerField()
	description = models.TextField(max_length=250)

	friends = models.ManyToManyField(Friend)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.destination

	def get_absolute_url(self):
		return reverse('trips_index')

class Itinerary(models.Model):
	date = models.DateField('activity date')
	activity = models.CharField(max_length=100)
	
	def __str__(self):
		return self.activity



class Photo(models.Model):
	url = models.CharField(max_length=250)
	trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

	def __str__(self):
		return f"Photo for trip_id: {self.trip_id} @{self.url}"

class Meta:
	ordering = ['-date'] 