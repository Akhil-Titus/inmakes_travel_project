from django.shortcuts import render
from django.http import HttpResponse
from . models import Place, Team
# Create your views here.

#Linking HTML to variables via ginger variable (passing value)
def home(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html",{'places':obj1, 'teams':obj2 } )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse('contact details')
#"""
def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    sum_ = x+y
    return render(request, 'result.html', {"result_obj":sum_} )
"""
def addition(request):
    return render(request, 'result.html')
 """