from django.urls import path
from guestbook import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path( "guestbook", views.guestbook, name="guestbook" ), # http://localhost:8000/guestbook/guestbook
    path( "write", views.write, name="write" ),                 # http://localhost:8000/guestbook/write
    path( "writepro", views.writepro, name="writepro" ),
    path( "passwdck", views.passwdck, name="passwdck" ),
    path( "update", views.update, name="update" ),
    path( "delete", views.delete, name="delete" ),
    #path( "writeform",views.writeform,name="writeform"),
    #path("writeform",views.WriteView.as_view())
     path("writeform",TemplateView.as_view(template_name="writeform.html"))
     
]