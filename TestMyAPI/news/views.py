from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
from rest_framework.parsers import JSONParser
from .serializers import *


@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        if serializer:
            return Response({'data': serializer.data, 'status': "OK"})
        else:
            return Response({'status': "ERR", 'errCode': 20}) #Internal server error

@csrf_protect
@api_view(('GET','POST'))
def setupNewProject(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': "OK"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': "ERR", 'errCode': 10})

@csrf_protect
@api_view(['GET', 'DELETE'])
def project_detail(requset, id):
    try:
        project = Project.objects.get(id=id)
        serializer = ProjectSerializer(project)
    except:
        return Response({'status': "ERR", 'errCode': 30}) # not found

    if requset.method == "GET":
            return Response({'data': serializer.data, 'status': "OK"})
    if requset.method == "DELETE":
            project.delete()
            return Response({'data': serializer.data, 'status': "OK"})

@api_view(['GET'])
def project_filter(request, pt):
    try:
        project = Project.objects.filter(ProjectType=pt)
        serializer = ProjectSerializer(project, many=True)
    except:
        return Response({'status': "ERR", 'errCode': 30})  # not found

    if request.method == "GET":
        return Response({'data': serializer.data, 'status': "OK"})

@csrf_protect
@api_view(['GET', 'POST'])
def NewProjectRequest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewProjectRequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'data': serializer.data, 'status': "OK"})
    else:
        return Response({'status': "ERR", 'errCode': 10})

@api_view(['POST'])
def NewConsultRequest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewConsultRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK'})
        else:
            return Response({'status': "ERR", 'errCode': 10})

