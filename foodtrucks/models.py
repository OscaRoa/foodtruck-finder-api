from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


class Foodtruck(models.Model):
    city = models.CharField(max_length=50, default='Mexico City')
    facebook = models.URLField()
    food_type = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=[city], zoom=7)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img/foodtrucks/', blank=True)
    price = models.IntegerField()
    rating = models.IntegerField()
    twitter = models.URLField()

    def __str__(self):
        return "\nName: {}\nRating: {}\nFoodtype: {}\n".format(self.name,
                                                               self.rating,
                                                               self.food_type)

    @property
    def location_parser(self):
        location_object = {}
        data = self.location.split(',')
        location_object['lat'] = data[0]
        location_object['long'] = data[1]
        return location_object


class Comment(models.Model):
    foodtruck = models.ForeignKey('Foodtruck')
    user = models.ForeignKey(User, default=1)
    comment = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0, null=True)
