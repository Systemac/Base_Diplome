from django.urls import path
from Diplome import views

urlpatterns = [
    path('', views.index)
]