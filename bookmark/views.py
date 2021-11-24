from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
def main( request ) :           # 흐름제어 / 처리된 데이터 연결 
    template = loader.get_template( "main.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )
    
def style( request ) :
    template = loader.get_template( "style.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def script( request ) :
    template = loader.get_template( "script.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def function( request ) :
    template = loader.get_template( "function.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def object( request ) :
    template = loader.get_template( "object.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def json( request ) :
    template = loader.get_template( "json.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery1( request ) :
    template = loader.get_template( "jquery1.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery2( request ) :
    template = loader.get_template( "jquery2.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery3( request ) :
    template = loader.get_template( "jquery3.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def study( request ) :
    template = loader.get_template( "study.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery4( request ) :
    template = loader.get_template( "jquery4.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery5( request ) :
    template = loader.get_template( "jquery5.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def jquery6( request ) :
    template = loader.get_template( "jquery6.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def ajax1( request ) :
    template = loader.get_template( "ajax1.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def ajax2( request ) :
    template = loader.get_template( "ajax2.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def user( request ) :
    template = loader.get_template( "user.html" )
    name = request.GET["name"]
    age = request.GET["age"]
    context = {
        "name": name,
        "age":age,
        }
    return HttpResponse( template.render( context, request ) )

def ajax3( request ) :
    template = loader.get_template( "ajax3.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def ajax4( request ) :
    template = loader.get_template( "ajax4.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def html1( request ) :
    template = loader.get_template( "html1.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def html2( request ) :
    template = loader.get_template( "html2.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def html3( request ) :
    template = loader.get_template( "html3.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )

def html4( request ) :
    template = loader.get_template( "html4.html" )
    context = {}
    return HttpResponse( template.render( context, request ) )





