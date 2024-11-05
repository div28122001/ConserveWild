from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import  profile


# Create your views here.
def registeration(request):
    if request.method=="POST":
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        un=request.POST["uname"]
        em=request.POST["ename"]
        pwdd=request.POST["pass"]
        cpw=request.POST["cpass"]
        cn=request.POST['con']
        
        if (pwdd==cpw):
            usr=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=pwdd)
            usr.save()
            ppf=profile(user=usr,cn=cn)
            ppf.save()
            return redirect("index.html")
        else:
            return redirect("contact.html")
            
        
    return render (request,"registration.html")

def login(request):
    if request.method=="POST":
        un=request.POST["un"]
        pwd=request.POST["pass"]
        usrlog=auth.authenticate(username=un,password=pwd)
        if usrlog != None:
            auth.login(request,usrlog)
            return redirect("index.html")
        else:
            return redirect("log")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("index.html")
def Profile(request):
    disp={}
    pro=profile.objects.filter(user__id=request.user.id)
    if len(pro)>0:
        entry=profile.objects.get(user__id=request.user.id)
        disp['prodisplay']=entry
    return render(request,"profile.html",disp)
def updateprofile(request):
    dis={}
    proid=profile.objects.filter(user__id=request.user.id)
    if len(proid)>0:
        entry=profile.objects.get(user__id=request.user.id)
        dis['disent']=entry
        if request.method=="POST":
            fnm=request.POST["fn"]
            lnm=request.POST["ln"]
            emm=request.POST["em"]
            cn=request.POST["con"]
            addr=request.POST["add"]
           

            usr=User.objects.get(id=request.user.id)
            usr.first_name=fnm
            usr.last_name=lnm
            usr.email=emm
            usr.save()

            entry.cn=cn
            entry.address=addr
            entry.save()
            if "pimg" in request.FILES:
                pro_image=request.FILES["pimg"]
                entry.pimg=pro_image
                entry.save()
            return redirect("pro")
        return redirect("pro")
    return render(request,'setting.html',dis)