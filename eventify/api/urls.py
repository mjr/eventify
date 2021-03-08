from django.urls import path, include

from rest_framework import routers

from eventify.subscriptions.views import SubscriptionViewSet


router = routers.SimpleRouter()
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]