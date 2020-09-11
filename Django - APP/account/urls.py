from django.urls import path
from account import views

urlpatterns = [
    path("login/",views.loginPage,name="LoginPage"),
    path("signup/",views.signupPage,name="SignupPage")
]
