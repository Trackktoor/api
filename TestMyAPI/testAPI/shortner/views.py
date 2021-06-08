from .models import *
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import NameForm

@csrf_protect
@api_view(('GET','POST'))
def URLs_list(request):
    if request.method == "GET":
        URLs = URL.objects.all()
        serializer = URLSerializer(URLs, many=True)
        if serializer:
            return Response({'data': serializer.data, 'status': "OK"})
        else:
            return Response({'status': "ERR", 'errCode': 20}) #Internal server error
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = URLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            URL_for_connect = URL.objects.get(full_url=(data['full_url']))
            url_hash = URL_hash.objects.create(url=URL_for_connect, user_agent=request.META.get('HTTP_USER_AGENT', ''), if_mobile=request.user_agent.is_mobile)
            url_hash.save()
            return Response({'data': serializer.data, 'status': "OK"})
        else:
            print(serializer.errors)
            return Response({'status': "ERR", 'errCode': 10}) #bed request
