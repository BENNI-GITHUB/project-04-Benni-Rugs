"""Services Models"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Service(models.Model):
    """ Model for Service """
    type = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        """Get url after superuser adds/edits service"""
        return reverse('services')

