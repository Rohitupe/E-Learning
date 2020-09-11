from django.shortcuts import render,redirect
from account.models import Account_info
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Account_info.objects.filter(email=email,password=password).exists():
            return redirect("HomePage")
        else:
            return render(request,'account/loginWrong.html')

        # print(obj)

    return render(request,'account/login.html')

def signupPage(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        ConfirmPassword = request.POST.get("confirmpassword")
        password = request.POST.get("password")
        
        print(first_name,last_name,email,password,ConfirmPassword)

        if first_name and last_name and email and password and ConfirmPassword is not None:
            if ConfirmPassword == password:
                if email is not None:
                    if Account_info.objects.filter(email=email).exists():
                        return render(request,'account/signupWrong.html')
                    else:
                        obj, created = Account_info.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, password=password, login_info=datetime.now())
                        return redirect("LoginPage")
        else:
            return render(request,'account/signupWrong.html')

    return render(request,'account/signup.html')