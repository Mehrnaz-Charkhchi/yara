from __future__ import unicode_literals

from django.db import models


class Purchase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField()
    purchase = models.CharField(max_length=150, blank=True, default='')
    purchase_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=150, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    email = models.CharField(max_length=150, blank=True, default='')
    address = models.TextField()

    class Meta:
        ordering = ('created',)
