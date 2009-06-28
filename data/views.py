from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse("<a href=\"test\">Hello World</a>")

def test(request):
    fields = ['test', 'foo']
    c = RequestContext(request, {'fields': fields})
    return render_to_response("data/test.html", c)
