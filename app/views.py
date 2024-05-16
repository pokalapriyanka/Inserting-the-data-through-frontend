from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic is inserted successfully')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        email=request.POST['email']
        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created successfully')

    return render(request,'insert_webpage.html')

def insert_access(request):
    if request.method=='POST':
        na=request.POST['na']
        date=request.POST['date']
        au=request.POST['au']
        RWO=Webpage.objects.get(name=na)
        AO=AccessRecord.objects.get_or_create(name=RWO,date=date,author=au)[0]
        AO.save()
        return HttpResponse('Access record is created successfully')

    return render(request,'insert_access.html')