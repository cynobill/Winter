from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("Hello shitheads!")