from __future__ import unicode_literals

from django.db import models
from ..login.models import User
import datetime
import re



class TripManager(models.Manager):
    def validate(self, postData):
        results = {
            'status': True,
            'errors': []
    }
        # field validation
        if len(postData['destination']) < 1:
            results['errors'].append('Please enter destination')
            results['status'] = False

        # current or future dates
        now = datetime.datetime.now()
        date = datetime.datetime.strptime(postData['date_from'],'%Y-%m-%d')
        if date < now:   # checking if date is before today!!!
            results['errors'].append("You cannot set a trip in the past!")
            results['status'] = False
        return results
    def add_trip(self, postData, user_id):
        new_trip = self.create( # logged_in user creates appntmnt
            destination = postData['destination'],
            description = postData['description'],
            date_from=postData['date_from'],
            date_to=postData['date_to'],
            users = User.objects.get(id = user_id)) # more here??!!
        new_trip.joined_by.add(new_trip.users)
        new_trip.save()
        return new_trip

    def joined(self, user_id, trip_id):
        trip = Trip.objects.get(id=trip_id)
        user_obj = User.objects.get(id=user_id)
        trip.joined_by.add(user_obj)
        trip.save()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    users = models.ForeignKey(User, related_name="added_by")
    joined_by = models.ManyToManyField(User, related_name="join_to")
    objects = TripManager()
