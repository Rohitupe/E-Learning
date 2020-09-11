from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from classes.models import ClassName, ClassSubject, ClassTopic

# Create your views here.

def classpage(request,id):
    class_name = get_object_or_404(ClassName,id=id)
    cSub = ClassSubject.objects.all()
    cTop = ClassTopic.objects.all()

    context = {
        'class_name':class_name,
        'class_subject' :cSub,
        'class_topic':cTop
    }

    return render(request,'classes/class.html',context)