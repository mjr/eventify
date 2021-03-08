from django.shortcuts import render

from rest_framework import mixins, viewsets

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
