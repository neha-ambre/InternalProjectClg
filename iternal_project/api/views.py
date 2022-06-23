import re
from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import AutisticData

# Create your views here.
def index(request):
    context={
        'variable':'this is sent'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

# def temp(request):
#     if request.method == 'POST':
#         firstName=request.POST.get('firstname')
#         address=request.POST.get('address')
#         refferedby=request.POST.get('refferedBy')
#         gender=request.POST.get('gender')
#         print(firstName,address,refferedby,gender)
#     return render(request,'temp.html')

def temp(request):
    form=DataForm()
    return render(request,'temp.html',{'form':form})

def saveForm(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        refferedby=request.POST.get('refferedby')
        autData=AutisticData(firstName=name,address=address,gender=gender,refferedBy=refferedby)
        autData.save()
    return HttpResponse('ok')