from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views 
def Insert_Topic(request):
    tn=input('enter Topic')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse("Topic data is inserted")
    
def Insert_webpage(request):
    tn=input('enter Topic')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    na=input('Enter name')
    u=input('Enter Url')
    wo=webpage.objects.get_or_create(topic_name=to,name=na,url=u)[0]
    wo.save()

    return HttpResponse('Webpage data is inserted')


def Insert_AccessRecord(request):
    tn=input('enter Topic')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    na=input('Enter name')
    u=input('Enter Url')
    wo=webpage.objects.get_or_create(topic_name=to,name=na,url=u)[0]
    wo.save()
    d=input('enter Date')
    a=input('enter Author')
    ao=AccessRecord.objects.get_or_create(topic_name=to,name=na,url=u,date=d,author=a)[0]
    ao.save()

    return HttpResponse('AccessRecord data is inserted')




