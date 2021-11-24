from django.contrib import admin
from guestbook.models import Guestbook
# 관리자가 관리할 DB 등록
class GuestbookAdmin( admin.ModelAdmin ) :
    list_display = ( "name", "email", "passwd", "content" )
admin.site.register( Guestbook, GuestbookAdmin )    

