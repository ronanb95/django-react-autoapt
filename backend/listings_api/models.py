from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Listing(models.Model):

    class ListingsObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('filtered', 'Filtered'),
        ('rented', 'Rented'),
    )
    
    area = models.ForeignKey(Area, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=options, default='published', max_length=25), 
    rooms = models.IntegerField()
    size = models.IntegerField()
    objects = models.Manager()  # default manager
    listingobjects = ListingsObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title