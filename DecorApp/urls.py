from django.urls import path
from DecorApp import views

urlpatterns=[
    path('homepage2/',views.homepage2,name="homepage2"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('productpage/<catname>/',views.productpage,name="productpage"),
    path('singlepage/<int:dataid>,<catname>/',views.singlepage,name="singlepage"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('savecart/',views.savecart,name="savecart"),
    path('deletecart/<int:dataid>',views.deletecart,name="deletecart"),
    path('',views.userpage,name="userpage"),
    path('usersavedata/',views.usersavedata,name="usersavedata"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('userlogout/',views.userlogout, name="userlogout"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('gallerypage/', views.gallerypage, name="gallerypage")

]