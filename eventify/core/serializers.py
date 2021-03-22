from rest_framework import serializers

from .models import Course, Talk


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ("title", "description", "start")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = TalkSerializer.Meta.fields + ("slots",)
