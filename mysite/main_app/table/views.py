
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  #table 페이지 
  return render(request, "table/table.html")

