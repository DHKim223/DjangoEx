from django.urls import path
from member import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path( "mainpage", views.mainpage, name="mainpage" ),   
    path( "register", TemplateView.as_view( template_name="register.html") ),
    path( "registerpro", views.registerpro, name="registerpro" ), 
    path( "confirm", views.confirm, name="confirm" ),
    path( "login", TemplateView.as_view( template_name="login.html"), name="login" ),
    path( "loginpro", views.loginpro, name="loginpro" ),
    path( "logout", views.logout, name="logout" ),
    path( "sidcheck", views.sidcheck, name="sidcheck" ),
    path( "delete", TemplateView.as_view( template_name="delete.html") ),
    path( "deletepro", views.deletepro, name="deletepro" ),
    path( "modify", TemplateView.as_view( template_name="modify.html") ),       
    path( "modifyview", views.modifyview, name="modifyview" ),
    path( "modifypro", views.modifypro, name="modifypro" ),
    path( "detail",views.detail,name = "detail"),
    
]
