from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.template import loader, Context, RequestContext

def index(request):

    return render(request, 'index.html')
