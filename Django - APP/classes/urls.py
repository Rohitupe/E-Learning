from django.urls import path
from classes import views

urlpatterns = [
    path("<int:id>/",views.classpage,name="ClassPage"),
]

