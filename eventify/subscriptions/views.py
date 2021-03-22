from django.conf import settings
from django.shortcuts import render

from rest_framework import mixins, viewsets

from eventify.core import mail

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        subscription = serializer.save()
        mail.send_mail(
            "Confirmação de Inscrição",
            settings.DEFAULT_FROM_EMAIL,
            subscription.email,
            "subscriptions/subscription_email.txt",
            {"subscription": subscription},
        )
