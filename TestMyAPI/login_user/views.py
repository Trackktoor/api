from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['name'], data['email'] or '', data['password'], is_staff=False, is_active=True)
            return Response({'status': "OK", 'data': f'{user}, был зарегестрирован'})
        except:
            return Response({'status': "ERR", 'errCode': 10})
