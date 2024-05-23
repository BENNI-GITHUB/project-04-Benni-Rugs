from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.about_us, name='about'),
    path('history/', views.history, name='history'),
    path('rug-weaving/', views.rug_weaving, name='weaving'),
    path('rug-repair/', views.rug_repair, name='repair'),
]