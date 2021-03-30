from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class DemoView(APIView):
    permission_classes = AllowAny,

    def get(self, *args, **kwargs):
        return Response({'detail': 'This is working!'})
