""" Contact Models """

from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """ Model for Contact """

    DESIGN_CONSULTATION = 'DS'
    PRODUCT_QUERY = 'PQ'
    ORDER_QUERY = 'OQ'
    DELIVERY_QUERY = 'DR'
    DELIVERY_INSURANCE = 'DI'
    RUG_REPAIR = 'RR'
    RUG_WASHING = 'RW'
    OTHER = 'O'
    ENQUIRY_CHOICES = [
        ('DESIGN_CONSULTATION', 'Rug Design Consultation'),
        ('PRODUCT_QUERY', 'Product Query'),
        ('ORDER_QUERY', 'Order Query'),
        ('DELIVERY_QUERY', 'Delivery Query'),
        ('DELIVERY_INSURANCE', 'Delivery and Insurance'),
        ('RUG_REPAIR', 'Rug Repair Services'),
        ('RUG_WASHING', 'Rug Washing Services'),
        ('OTHER', 'Other')
        ]

    name = models.CharField(max_length=122, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    enquiry_type = models.CharField(
        max_length=254, choices=ENQUIRY_CHOICES, default='DS')
    message = models.TextField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url after user submits enquiry """
        return reverse('home')

    class Meta:
        """ To display the equiries by date in ascending order """
        ordering = ['-date']

    def __str__(self):
        return f"Enquiry: {self.enquiry_type} from {self.name}"