from django.shortcuts import render, redirect
import logging
from django.template import loader
from django.http.response import HttpResponse
from board.models import Board
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from BoardEx.settings import PAGE_SIZE
logger = logging.getLogger( __name__ )

# Create your views here.

def mainpage( request ) :
    template = loader.get_template( "mainpage.html" )
    memid = request.session.get("memid")
    if memid :
        context = {
            "memid":memid,
        }
    else :
        context = {}
    return HttpResponse( template.render( context, request ) )

@ csrf_exempt
def registerpro(request):
    dto = Member(
            id = request.POST["id"],
            passwd = request.POST["passwd"],
            name = request.POST["name"],
            student_id = request.POST["student_id"],
            department = request.POST["department"],
            grade = request.POST["grade"],
            level = request.POST["level"],
            join_date = DateFormat(datetime.now()).format("Y-m-d")
        )
    dto.save()
    return redirect("login")
    
import logging
logger = logging.getLogger(__name__)

    
@csrf_exempt
def confirm(request):
    template = loader.get_template("confirm.html")
    id = request.GET["id"]
    
    try :
        Member.objects.get(id=id)
        # 아이디가 있다.
        result = 1
    except ObjectDoesNotExist :
        # 아이디가 없다.
        result =0
        
    context={
        "result" : result,
        "id" : id
        }
    logger.info("confirm : " +str(result))
    return HttpResponse(template.render(context,request))

@csrf_exempt    
def loginpro( request ) :
    id = request.POST["id"]
    passwd = request.POST["passwd"]
    msg = ""
    template = loader.get_template( "login.html" )
    try :
        # 아이디가 있다
        dto = Member.objects.get(id=id)
        if passwd == dto.passwd :
            # 비밀번호가 같다
            request.session["memid"] = id
            return redirect( "mainpage" )        
        else :
            # 비밀번호가 다르다
            msg = "비밀번호가 다릅니다."      
    except ObjectDoesNotExist :
        # 아이디가 없다
        msg = "입력하신 아이디가 없습니다."
        
    context = {
        "msg" : msg
        }        
    return HttpResponse( template.render( context, request ) )

def logout(request):
    del (request.session["memid"])
    return redirect("mainpage")

@csrf_exempt
def sidcheck(request):
    keyword = request.POST["keyword"]
    dots = Member.objects.all()
    check = False
    for dto in dots :
        if keyword==dto.student_id :
            check= TRUE
            break;
        
    if check : 
        return HttpResponse("존재하는 학번입니다.")
    else :
        return HttpResponse("사용가능한 학번입니다.")
    
# 회원탈퇴
@csrf_exempt
def deletepro( request ) :
    id = request.session.get( "memid" )
    passwd = request.POST["passwd"]
    dto= Member.objects.get( id = id )
    if passwd == dto.passwd :
        dto.delete()
        del( request.session["memid"] )
        return redirect( "mainpage" )
    else :
        template = loader.get_template( "delete.html" )
        context = {
            "msg" : "입력하신 비밀번호가 다릅니다."
            }
        return HttpResponse( template.render( context, request ) )
    
# 회원정보수정
@csrf_exempt
def modifyview( request ) :
    id = request.session.get( "memid" )
    passwd = request.POST["passwd"]
    dto = Member.objects.get( id = id )
    if passwd == dto.passwd :
        template = loader.get_template( "modifyview.html" )        
        context = {
            "dto" : dto
            }
    else :
        template = loader.get_template( "modify.html" )
        context = {
            "msg" : "입력하신 비밀번호가 다릅니다."
            }
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def modifypro(request):
    id = request.session.get("memid")
    dto = Member.objects.get(id=id)
    dto.passwd = request.POST["passwd"]
    dto.department = request.POST["department"]
    dto.grade = request.POST["grade"]
    dto.level = request.POST["level"]
    dto.save()
    
    return redirect("mainpage")

# 글 보기
def detail(request):
    num = request.GET.get("num")
    pagenum = request.GET.get("pagenum")
    template = loader.get_template("detail.html")
    
    dto = Board.objects.get(num = num)
    context = {
        "dto" : dto,
        "pagenum" : pagenum,
        }
    
    return HttpResponse(template.render(context,request))
