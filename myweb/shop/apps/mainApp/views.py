from django.shortcuts import render

def index(request):
    context={
        'title':"خوش امدید"
        }
    return render(request,"mainApp/index.html",context)
