from django.urls import path, include

from rest_framework import routers

from eventify.core.views import TalkViewSet
from eventify.subscriptions.views import SubscriptionViewSet


router = routers.SimpleRouter()
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'talks', TalkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]