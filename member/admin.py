from django.contrib import admin
from member.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","name","student_id","department", "grade","level","join_date")
admin.site.register(Member, MemberAdmin)
    