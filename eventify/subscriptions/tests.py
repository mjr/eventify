from django.core import mail

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Subscription


class SubscriptionsGet(APITestCase):
    def setUp(self):
        self.resp = self.client.get("/api/v1/subscriptions/")

    def test_get(self):
        """Get /api/v1/subscriptions/ must return status code 405"""
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, self.resp.status_code)


class SubscriptionsPostValid(APITestCase):
    def setUp(self):
        data = {
            "name": "Test",
            "cpf": "00000000000",
            "email": "test@email.com",
            "phone": "(00) 00000-0000",
        }
        self.resp = self.client.post("/api/v1/subscriptions/", data)

    def test_post(self):
        """Valid POST to /api/v1/subscriptions/ must return status code 201"""
        self.assertEqual(status.HTTP_201_CREATED, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsPostInvalid(APITestCase):
    def setUp(self):
        self.resp = self.client.post("/api/v1/subscriptions/", {})

    def test_post(self):
        """Invalid POST must return status code 400"""
        self.assertEqual(status.HTTP_400_BAD_REQUEST, self.resp.status_code)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class SubscriptionsPatch(APITestCase):
    def setUp(self):
        self.resp = self.client.patch("/api/v1/subscriptions/")

    def test_patch(self):
        """Patch /api/v1/subscriptions/ must return status code 405"""
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, self.resp.status_code)


class SubscriptionsPut(APITestCase):
    def setUp(self):
        self.resp = self.client.put("/api/v1/subscriptions/")

    def test_put(self):
        """Put /api/v1/subscriptions/ must return status code 405"""
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, self.resp.status_code)


class SubscriptionsDelete(APITestCase):
    def setUp(self):
        self.resp = self.client.delete("/api/v1/subscriptions/")

    def test_delete(self):
        """Delete /api/v1/subscriptions/ must return status code 405"""
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, self.resp.status_code)