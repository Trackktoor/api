from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.conf import settings
from django.core.mail import send_mail
import requests
from django.views.decorators.csrf import csrf_protect
from django.db.models import F

from .serializers import *


@api_view(['GET', 'POST'])
def all_projects(request):
    if request.method == "GET":
        Projects = project.objects.all()
        serializer = ProjectSerializer(Projects, many=True)
        if serializer:
            return Response({'data': serializer.data, 'status': "OK"})
        else:
            return Response({'status': "ERR", 'errCode': 502})


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
        return Response({'status': "ERR", 'errCode': 502})

    if requset.method == "GET":
        return Response({'data': serializer.data, 'status': "OK"})
    if requset.method == "DELETE":
        Project.delete()
        return Response({'data': {}, 'status': "OK"})


@api_view(['GET'])
def projects_by_type(request, pt):
    projects = list(
        project.objects.annotate(project_filter=F('project_type').bitand(pt)).filter(project_filter__gte=pt))
    all_projects = list(project.objects.all())

    for el in all_projects:
        if el in projects:
            continue
        else:
            projects.append(el)

    serializer = ProjectSerializer(projects, many=True)

    if request.method == "GET":
        return Response({'data': serializer.data, 'status': "OK"})


@csrf_protect
@api_view(['GET', 'POST'])
def new_project_request(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        connection = psycopg2.connect(
            user="postgres",
            password="roma.ru12",
            host="127.0.0.1",
            port="5432",
            database="DB_for_bot_2")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()

        cursor.execute("SELECT USER_ID from MAIN")
        info = cursor.fetchall()
        for user_id in info:
            response = requests.post(
                url='https://api.telegram.org/bot1833138112:AAH4WaldLi4tzlG2yPPk2g_NYqxsq-t4xOk/sendMessage',
                data={'chat_id': user_id[0], 'text': str(data)}
            ).json()

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
        print(str(data))
        serializer = NewConsultRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': {}, 'status': 'OK'})
        else:
            return Response({'status': "ERR", 'errCode': 502})


@api_view(['POST', 'GET'])
def send_post_request_telegram_bot(request):
    if request.method == 'POST':
        response = requests.post(
            url='https://api.telegram.org/bot1828586591:AAFxq3ejfoft126qb8u-Mh1NgnkLtfa7o3w/sendMessage',
            data={'chat_id': -538035856, 'text': request.POST["name"]}
        ).json()

        response = requests.post(f'https://api.telegram.org/bot1828586591:AAFxq3ejfoft126qb8u-Mh1NgnkLtfa7o3w/sendDocument',
                          data={'chat_id': -538035856},
                          files={"document": request.FILES['document']}
        ).json()

        response = requests.post(
                        url='https://api.telegram.org/bot1828586591:AAFxq3ejfoft126qb8u-Mh1NgnkLtfa7o3w/sendMessage',
                        data={'chat_id': -538035856, 'text': request.POST["msg"]}
        ).json()

    return Response({"data": "da", "status": ')'})

@csrf_protect
@api_view(['GET', 'POST'])
def get_all_commits_in_GIT(request, author, repos):
    if request.method == "GET":
        data = {}
        commits = requests.get('https://api.github.com/repos/{0}/{1}/commits'.format(author, repos)).json()

        for commit in commits:
            if len(commit["parents"]) != 0:
                data[commit["commit"]["message"]] = {
                    "author": commit["commit"]["author"]["name"],
                    "date": commit["commit"]["author"]["date"],
                    "additions": (requests.get(commit["parents"][0]["url"]).json())["stats"]

                }

        return Response(data)