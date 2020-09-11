from django.urls import path
from subjects import views

urlpatterns = [
    path("",views.subjectPage,name="SubjectPage"),
    path("<int:id>/",views.videoPage,name="VideoPage"),
    path("message/",views.messagePage,name="MessagePage")
]
