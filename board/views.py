import io

from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Board
from .serializers import BoardSerializer


# Create your views here.

class BoardAPIView(APIView):
    def get(self, request, pk):
        lst = Board.objects.filter(user_id=pk).values()
        return Response({'items': list(lst)})

    def post(self, request):
        post_new = Board.objects.create(
            title=request.data['title'],
            items_id=request.data['items_id'],
            user_id=request.data['user_id'],
        )
        return Response({'post': model_to_dict(post_new)})

    def delete(self, request, pk):
        transformer = Board.objects.filter(id=pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all().values()
        return Response({'users': list(users)})