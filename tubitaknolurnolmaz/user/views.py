from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,get_user_model,logout
from django_email_verification import sendConfirm

  

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST or None)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            email=form.cleaned_data.get("email") 

            new_user = User.objects.create(username=username, email=email, password=password)
            
            sendConfirm(new_user)
            new_user.save()
            login(request,new_user)
            messages.success(request,"Başarıyla kayıt oldunuz...")
            return redirect("index")
        context ={
            "form":form
        }
        return render(request,"register.html",context)
    else:
        form=RegisterForm()
        context ={
            "form":form
        }
        return render(request,"register.html",context)
    """
    form=RegisterForm()
    context = {
        "form" : form,
    }
    return render(request,"register.html",context)"""

def loginUser(request):
    form=LoginForm(request.POST or None)
    
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")