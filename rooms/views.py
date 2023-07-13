from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):  # object request를 무지성으로 받는다.
    return HttpResponse("hello!")
