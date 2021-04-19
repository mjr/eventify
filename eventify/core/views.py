from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Talk
from .serializers import CourseSerializer, TalkSerializer, ScheduleSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ScheduleView(APIView):
    def get(self, request, format=None):
        serializer = ScheduleSerializer(
            {"talks": Talk.objects.all(), "courses": Course.objects.all()}
        )
        return Response(serializer.data)
