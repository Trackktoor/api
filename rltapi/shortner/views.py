from .models import *

from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view


@csrf_protect
@api_view(('GET', 'POST'))
def URLs_list(request):
    if request.method == "GET":
        URLs = []
        for url in URL.objects.all():
            URLs.append(url.get_info())
        return Response({'data': URLs, 'status': "OK"})



def click_test_redirection_view(request, url_hash):
    if request.method == 'GET':
        url = get_object_or_404(URL, short_url=url_hash)
        url.clicked()

        URL_for_connect = URL.objects.get(url=(url.url))

        url_hash = URL_hash.objects.create(url=URL_for_connect, user_agent=request.META.get('HTTP_USER_AGENT', ''),
                                           if_mobile=request.user_agent.is_mobile, ip=request.META.get('REMOTE_ADDR', ''))
        url_hash.save()

        return redirect(url.url)


@csrf_protect
@api_view(('GET', 'POST'))
def add_new_short_link(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = URLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            URL_for_connect = URL.objects.get(url=(data['url']))
            print(8795)
            print(request.META.get('REMOTE_ADDR', ''))
            url_hash = URL_hash.objects.create(url=URL_for_connect, user_agent=request.META.get('HTTP_USER_AGENT', ''),
                                               if_mobile=request.user_agent.is_mobile, ip=request.META.get('REMOTE_ADDR', ''))
            url_hash.save()
            return Response({'data': {"short_url": serializer.data['short_url']}, 'status': "OK"})
        else:
            return Response({'status': "ERR", 'errCode': 502})

@csrf_protect
@api_view(('GET', 'POST'))
def get_info_for_url(requset, short_url_hash):
    if requset.method == 'GET':
        url = get_object_or_404(URL, short_url=short_url_hash)
        urls_hash = []

        for url in URL_hash.objects.filter(url=url):
            urls_hash.append(url.get_info())

        return Response({'data': urls_hash, 'status': "OK"})

        return Response({"data": urls_hash})
