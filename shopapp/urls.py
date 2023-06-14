from django.urls import path
from shopapp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('addpage/',views.addpage,name="addpage"),
    path('savedata/',views.savedata,name="savedata"),
    path('displaycat/',views.displaycat,name="displaycat"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('updatecat/<int:dataid>/', views.updatecat, name="updatecat"),
    path('deletecat/<int:dataid>/', views.deletecat, name="deletecat"),
    path('addpro/',views.addpro,name="addpro"),
    path('savepro/',views.savepro,name="savepro"),
    path('displaytpro/',views.displaytpro,name="displaytpro"),
    path('editpro/<int:dataid>',views.editpro,name="editpro"),
    path('updatepro/<int:dataid>',views.updatepro,name="updatepro"),
    path('deletepro/<int:dataid>',views.deletepro,name="deletepro"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
]