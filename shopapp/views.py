from django.shortcuts import render,redirect
from django.http import  HttpResponse
from shopapp.models import firstdb,seconddb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def addpage(request):
    return render(request,"addcategory.html")
def savedata(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        ty=request.POST.get('types')
        de=request.POST.get('description')
        img=request.FILES['image']
        obj=firstdb(Name=na,Types=ty,Description=de,Image=img)
        obj.save()
        messages.success(request, "Category Added.. Successfully..!")

        return redirect(addpage)

def displaycat(request):
     data = firstdb.objects.all()
     return render(request, "displaycategory.html", {"data": data})

def editcat(request,dataid):
    data=firstdb.objects.get(id=dataid)
    print(data)
    return render(request,"editcategory.html",{"data":data})

def updatecat(request,dataid):
    if request.method=="POST":
        na = request.POST.get('Name')
        ty = request.POST.get('types')
        de = request.POST.get('description')
        img = request.FILES['image']
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=firstdb.objects.get(id=dataid).image
        firstdb.objects.filter(id=dataid).update(Name=na,Types=ty,Description=de,Image=img)
        return redirect(displaycat)

def deletecat(request,dataid):
    data=firstdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Category Deleted..!")
    return redirect(displaycat)

def addpro(request):
    data= firstdb.objects.all()
    return render(request,"addproduct.html",{"data":data})

def savepro(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        co=request.POST.get('Colour')
        ca = request.POST.get('Category')
        pr=request.POST.get('Price')
        des=request.POST.get('Description')
        img=request.FILES['Image']
        obj=seconddb(Name=na,Colour=co,Category=ca,Price=pr,Description=des,Image=img)
        obj.save()
        messages.success(request, "Product Added..!")

        return redirect(addpro)

def displaytpro(request):
    data = seconddb.objects.all()
    return render(request,"displayproduct.html",{"data":data})

def editpro(request,dataid):
    data=seconddb.objects.get(id=dataid)
    print(data)
    return render(request,"editproduct.html",{"data":data})


def updatepro(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ca = request.POST.get('category')
        co = request.POST.get('colour')
        pr = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES['image']
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=seconddb.objects.get(id=dataid).image
        seconddb.objects.filter(id=dataid).update(Name=na,Category=ca,Colour=co,Price=pr,Description=des,Image=img)
        return redirect(displaytpro)


def deletepro(request,dataid):
    data=seconddb.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Product Deleted..!")

    return redirect(displaytpro)
def loginpage(request):
    return render(request,"adminlogin.html")
def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(homepage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)







