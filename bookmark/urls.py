from django.urls import path
from bookmark import views
urlpatterns = [
    path( "", views.main, name="" ),                          # HTML http://localhost:8000/bookmark
    path( "style/", views.style, name="style" ),             # CSS    http://localhost:8000/bookmark/style
    path( "script", views.script, name="script" ),            # Javascript 기본
    path( "function", views.function, name="function" ),    # Javascript 함수     
    path( "object", views.object, name="object" ),          # Javascript 클래스 이벤트
    path( "json", views.json, name="json" ),                  # JQuery JSON  
    path( "jquery1", views.jquery1, name="jquery1" ),       # JQuery 선택자
    path( "jquery2", views.jquery2, name="jquery2" ),      # JQuery 함수
    path( "jquery3", views.jquery3, name="jquery3" ),      # JQuery 문서 관련 함수
    path( "study", views.study, name="study" ),             # 과제
    path( "jquery4", views.jquery4, name="jquery4" ),      # JQuery 객체 추가
    path( "jquery5", views.jquery5, name="jquery5" ),      # JQuery 이벤트
    path( "jquery6", views.jquery6, name="jquery6" ),      # JQuery 이벤트
    
    path( "ajax1", views.ajax1, name="ajax1" ),              # Ajax 기본
    path( "ajax2", views.ajax2, name="ajax2" ),             # JQuery + Ajax 
    path( "user", views.user, name="user" ),                 # Ajax 데이터 처리
    path( "ajax3", views.ajax3, name="ajax3" ),             # Ajax XML 데이터 처리
    path( "ajax4", views.ajax4, name="ajax4" ),             # Ajax JSON 데이터 처리
    
    path( "html1", views.html1, name="html1" ),             # 
    path( "html2", views.html2, name="html2" ),             #
    path( "html3", views.html3, name="html3" ),             #
    path( "html4", views.html4, name="html4" ),             #
    
    
]









