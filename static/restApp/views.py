from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from .models import Poll
from rest_framework.response import Response
from restApp.serializers import UserSerializer, GroupSerializer, PollSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

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

class poll_list(APIView):
    """
    List all code polls, or create a new poll.
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PollSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class poll_detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """             
    permission_classes = (AllowAny,)

    def get_object(self, pk):
	    try:
	        return Poll.objects.get(pk=pk)
	    except Poll.DoesNotExist:
	        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
    	poll = self.get_object(pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
    	poll = self.get_object(pk)
        serializer = PollSerializer(poll, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
    	poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)