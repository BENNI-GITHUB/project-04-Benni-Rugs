"""imports for admin page"""

from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    """Allows admin to manage Testimonials via the admin panel"""
    list_display = (
        'name',
        'service',
        'created_on'
    )

admin.site.register(Testimonial, TestimonialAdmin)