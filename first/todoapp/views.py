from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def hello(request):
    return HttpResponse(f"<h1> random number: {random.randint(1,1000)}</h1>")