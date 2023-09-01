from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views 
def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def Insert_Topic(request):
    tn=input('enter Topic')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

    
def display_webpage(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
    
def Insert_webpage(request):
    tn=input('enter Topic')
    to=Topic.objects.get_or_create(topic_name=tn)
    na=input('Enter name')
    u=input('Enter Url')
    wo=webpage.objects.get_or_create(topic_name=to,name=na,url=u)[0]
    wo.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_accessrecord.html',d)


def Insert_AccessRecord(request):
    pk=input('Enter a Number')
   
    d=input('enter Date')
    a=input('enter Author')
    wo=webpage.objects.get(pk=pk)
    ao=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}

    return render(request,'display_accessrecord.html',d)









































