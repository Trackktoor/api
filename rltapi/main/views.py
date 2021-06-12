from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
from rest_framework.parsers import JSONParser
from .serializers import *


@api_view(['GET', 'POST'])
def all_projects(request):
    if request.method == "GET":
        Projects = project.objects.all()
        serializer = ProjectSerializer(Projects, many=True)
        if serializer:
            return Response({'data': serializer.data, 'status': "OK"})
        else:
            return Response({'status': "ERR", 'errCode': 502}) #Internal server error

@csrf_protect
@api_view(('GET', 'POST'))
def create_new_project(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': {}, 'status': "OK"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': "ERR", 'errCode': 502})

@csrf_protect
@api_view(['GET', 'DELETE'])
def project_detail(requset, id):
    try:
        Project = project.objects.get(id=id)
        serializer = ProjectSerializer(Project)
    except:
        return Response({'status': "ERR", 'errCode': 502}) # not found

    if requset.method == "GET":
            return Response({'data': serializer.data, 'status': "OK"})
    if requset.method == "DELETE":
            Project.delete()
            return Response({'data': {}, 'status': "OK"})

@api_view(['GET'])
def projects_by_type(request, pt):
    try:
        Projects = project.objects.filter(project_type=pt)
        serializer = ProjectSerializer(Projects, many=True)
    except:
        return Response({'status': "ERR", 'errCode': 502})  # not found

    if request.method == "GET":
        return Response({'data': serializer.data, 'status': "OK"})

@csrf_protect
@api_view(['GET', 'POST'])
def new_project_request(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewProjectRequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': {}, 'status': "OK"})
    else:
        return Response({'status': "ERR", 'errCode': 502})

@api_view(['POST'])
def new_consult_request(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewConsultRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': {}, 'status': 'OK'})
        else:
            return Response({'status': "ERR", 'errCode': 502})

