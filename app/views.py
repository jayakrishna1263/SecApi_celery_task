from django.shortcuts import render
from django.http import HttpResponse

from .tasks import fetch_filings_task

# Create your views here.

def fetchApi(request):
    
    fetch_filings_task()
    return HttpResponse("Succesfully fetched")