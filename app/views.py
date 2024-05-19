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
    #updation of the records
    Webpage.objects.filter(name='Priya').update(url='http://p.in')
    Webpage.objects.filter(url='http://dk.in').update(email='dinesh@gmail.com')
    Webpage.objects.update_or_create(name='Dhoni',defaults={'url':'http://msd.in'})
    #deletion of the records
    Webpage.objects.filter(name='Pallavi').delete()
    Webpage.objects.filter(url='http://d.in').delete()
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        email=request.POST['email']
        RTO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=RTO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created successfully')

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    #updation of the records
    AccessRecord.objects.filter(id=6).update(author='Pallavikiran')
    AccessRecord.objects.filter(author='Dinesh Karthik').update(date='1982-05-12')
    AccessRecord.objects.update_or_create(date='2001-03-10',defaults={'author':'Priya yadav'})
    #deletion of the records
    AccessRecord.objects.filter(author='Mutkundu kirti').delete()
    AccessRecord.objects.filter(id=3).delete()
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        date=request.POST['date']
        au=request.POST['au']
        RWO=Webpage.objects.get(id=na)
        AO=AccessRecord.objects.get_or_create(name=RWO,date=date,author=au)[0]
        AO.save()
        return HttpResponse('Access record is created successfully')

    return render(request,'insert_access.html',d)



def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        STL=request.POST.getlist('tn')
        WOS=Webpage.objects.none()
        for t in STL:
            WOS=WOS|Webpage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)


def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)