from django.shortcuts import render

from rest_framework import viewsets

from .models import Talk
from .serializers import TalkSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
