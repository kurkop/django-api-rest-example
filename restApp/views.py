from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Poll
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from restApp.serializers import UserSerializer, GroupSerializer, PollSerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def index_view(request):
    return HttpResponse("Respuesta :D")

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def poll_list(request):
    """
    List all code polls, or create a new poll.
    """

    if request.method == 'GET':
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PollSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def poll_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """              
    try:
        poll = Poll.objects.get(pk=pk)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PollSerializer(poll, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)