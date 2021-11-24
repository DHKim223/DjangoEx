from django.shortcuts import render, redirect
from django.template import loader
from django.http.response import HttpResponse
from guestbook.models import Guestbook
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.views.generic.base import View

def guestbook( request ) : 
    template = loader.get_template( "guestbook.html" )
    gbcount = Guestbook.objects.count()             # 글수
    gblist = Guestbook.objects.order_by("-idx")     # 전체글 내림차순
    context = {
        "gbcount" : gbcount,
        "gblist" : gblist
    }
    return HttpResponse( template.render( context, request ) )

def write( request ) : 
    template = loader.get_template( "write.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )
    
@csrf_exempt    
def writepro( request ) :
    dto = Guestbook( name=request.POST["name"],
               email=request.POST["email"],
               passwd=request.POST["passwd"],
               content=request.POST["content"] )
    dto.save()          # insert 호출
    return redirect( "guestbook" )

@csrf_exempt   
def passwdck( request ) :    
    idx = request.POST["idx"]
    passwd = request.POST["passwd"]
    dto = Guestbook.objects.get( idx = idx )
    context = {
        "dto" : dto,
        }
    if passwd == dto.passwd :
        # 수정 / 삭제 페이지
        template = loader.get_template( "edit.html" )
        return HttpResponse( template.render( context, request ) )
    else :
        # 방명록 페이지 
        return redirect( "guestbook" )
    
@csrf_exempt       
def update( request ):
    idx = request.POST["idx"]
    email=request.POST["email"]
    passwd=request.POST["passwd"]
    content=request.POST["content"]
    dto = Guestbook.objects.get(idx=idx)    # 원본
    newdto = Guestbook(
        idx=idx,
        name = dto.name,
        email = email,
        passwd = passwd,
        content=content
        )
    newdto.save()
    return redirect("guestbook")

def delete( request ):
    idx = request.GET["idx"]
    Guestbook.objects.get(idx=idx).delete()
    return redirect("guestbook")

# 폼 클래스 생성--HTML 대신
class Writeform(forms.Form):
    name = forms.CharField(label="name",max_length="50")
    email = forms.EmailField(label="email",max_length = "100")
    passwd = forms.CharField(label="passwd",max_length="20", widget=forms.PasswordInput,required=True)
    content = forms.CharField ( label = "content", widget=forms.Textarea)
    
    

def writeform(request):
    template = loader.get_template("writeform.html")
    context = {
        "form":Writeform
        }
    return HttpResponse(template.render(context,request))

class WriteView(View):
    def get(self, request):
         template = loader.get_template("writeform.html")
         context = {
             "form":Writeform
        }
         return HttpResponse(template.render(context,request))

    def post(self, request):       
         pass
       

    
    





