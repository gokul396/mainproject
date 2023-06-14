from django.shortcuts import render,redirect
from shopapp.models import firstdb,seconddb
from DecorApp.models import cartdb,userdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
def homepage2(request):
    data = firstdb.objects.all()
    return render(request,"1home.html",{"data":data})
def aboutpage(request):
    data = firstdb.objects.all()
    return render(request,"about.html",{"data":data})

def productpage(request, catname):
        data = firstdb.objects.all()
        product = seconddb.objects.filter(Category=catname)
        return render(request, "product.html", {'data': data, 'product': product})
def singlepage(request,dataid,catname):
    # data = firstdb.objects.all()
    # product = seconddb.objects.filter(Category=catname)
    data= seconddb.objects.all()
    products=seconddb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'data':data,'products':products})
def cartpage(request,):
    # car = cartdb.objects.filter(user=request.session['username'])
    # products=seconddb.objects.get(id=dataid)
    car = cartdb.objects.all()
    return render(request, "cart.html",{'car':car})
def savecart(request):
    if request.method=="POST":
        pn=request.POST.get('productnamee')
        pq=request.POST.get('productqut')
        un=request.POST.get('user')
        tp=request.POST.get('totalprice')
        pp=request.POST.get('productprice')
        obj=cartdb(productname=pn,productqut=pq,totalprice=tp,user=un,productprice=pp)
        obj.save()
        return redirect(homepage2)
def deletecart(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "Product Removed from Cart..!")

    return redirect(cartpage)

def userpage(request):
   return render(request,"userlogin.html")

def usersavedata(request):
    if request.method=="POST":
        user_r=request.POST.get('usernamel')
        gmail_r = request.POST.get('email')
        password_r=request.POST.get('passwordl')
        c_password=request.POST.get('conformpasswordl')
        obj=userdb(username=user_r,email=gmail_r,password=password_r,confirmpassword=c_password)
        obj.save()
        messages.success(request, " ,Account Created Successfully..!")
        return redirect(userpage)

def userloginpage(request):
        if request.method == "POST":
            username_R = request.POST.get('usernamel')
            password_R = request.POST.get('passwordl')
            if userdb.objects.filter(username=username_R,password=password_R).exists():
                # data=userdb.objects.filter(username=username_R,password=password_R).values('email','id').first()

                request.session['username']=username_R

                request.session['password']=password_R

                return redirect(homepage2)

            else:
                  return redirect(userpage)
        else:
             return redirect(userpage)
def userlogout(request):
    if request.session:
        request.session.clear()
    return redirect(userloginpage)

def checkoutpage(request):
    return render (request,"checkout.html")
def contactpage(request):
    return render (request,"contact.html")
def gallerypage(request):
    return render (request,"gallery.html")

