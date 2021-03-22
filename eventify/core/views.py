from django.shortcuts import render

from rest_framework import viewsets

from .models import Course, Talk
from .serializers import CourseSerializer, TalkSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
