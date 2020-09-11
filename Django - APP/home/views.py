from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from subjects.models import Subject
from classes.models import ClassName

# Create your views here.
def homePage(request):
    class_name = ClassName.objects.all()

    allSubject = Subject.objects.order_by('-id')[:6]
    # send Email From CONTACT section
    if request.method == "POST":
        Fname = request.POST.get('Name')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')

        send_mail(
            f"E-learning Message From {Email}",
            f"Message From {Fname} - {Message}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        return redirect("HomePage")
    return render(request,'home/index.html',{'subject':allSubject,'className':class_name})

def pricePage(request):
    return render(request,'home/pricing.html')
