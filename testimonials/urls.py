from django.urls import path
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='testimonials'),
    path('add/', views.AddTestimonial.as_view(), name='add_testimonial'),
    path('edit/<int:pk>/', views.EditTestimonial.as_view(), name='edit_testimonial'),
    path('delete/<int:pk>/', views.DeleteTestimonial.as_view(), name='delete_testimonial'),
]