from . import views
from django.urls import path

urlpatterns = [
    path('waiting', views.waiting, name='waiting'),
]
