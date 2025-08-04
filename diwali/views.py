from django.shortcuts import render
import datetime

# Create your views here.
now = datetime.datetime.now()
def index(request):
    return render(request , "diwali/index.html",{
        "diwali" : now.month == 9 and now.day == 20
    })