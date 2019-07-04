from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('valleyapp/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('valleyapp/create.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
