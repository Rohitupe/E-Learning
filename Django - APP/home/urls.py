from django.urls import path
from home import views

urlpatterns = [
    path("",views.homePage, name="HomePage"),
    path("price/",views.pricePage,name="PricePage"),
]
