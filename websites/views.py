from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the web planner")


def date(request):
    return HttpResponse("This page was saved at " + str(datetime.now()))

# Please add an About page
