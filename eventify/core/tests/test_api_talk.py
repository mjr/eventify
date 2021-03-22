from django.core import mail

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Talk


class TalksGet(APITestCase):
    def setUp(self):
        Talk.objects.create(
            title="Rust",
            description="Uma linguagem capacitando todos a construir softwares confiáveis e eficientes.",
            start="08:00:00",
        )
        self.resp = self.client.get("/api/v1/talks/")

    def test_get(self):
        """Get /api/v1/talks/ must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.resp.status_code)

    def test_data(self):
        self.assertEqual(
            self.resp.data,
            [
                {
                    "title": "Rust",
                    "description": "Uma linguagem capacitando todos a construir softwares confiáveis e eficientes.",
                    "start": "08:00:00",
                }
            ],
        )


class TalksPostValid(APITestCase):
    def setUp(self):
        data = {
            "title": "Go",
            "description": "Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.",
            "start": "10:00:00",
        }
        self.resp = self.client.post("/api/v1/talks/", data)

    def test_post(self):
        """Valid POST to /api/v1/talks/ must return status code 201"""
        self.assertEqual(status.HTTP_201_CREATED, self.resp.status_code)

    def test_save_talk(self):
        self.assertTrue(Talk.objects.exists())


class TalksPostInvalid(APITestCase):
    def setUp(self):
        self.resp = self.client.post("/api/v1/talks/", {})

    def test_post(self):
        """Invalid POST must return status code 400"""
        self.assertEqual(status.HTTP_400_BAD_REQUEST, self.resp.status_code)

    def test_dont_save_talk(self):
        self.assertFalse(Talk.objects.exists())


class TalksPatchValid(APITestCase):
    def setUp(self):
        Talk.objects.create(
            title="Rust",
            description="Uma linguagem capacitando todos a construir softwares confiáveis.",
            start="08:00:00",
        )
        self.resp = self.client.patch(
            "/api/v1/talks/1/",
            {
                "description": "Uma linguagem capacitando todos a construir softwares confiáveis e eficientes."
            },
        )

    def test_patch(self):
        """Patch /api/v1/talks/1/ must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.resp.status_code)


class TalksPutValid(APITestCase):
    def setUp(self):
        Talk.objects.create(
            title="Rust",
            description="Uma linguagem capacitando todos a construir softwares confiáveis e eficientes.",
            start="08:00:00",
        )
        self.resp = self.client.put(
            "/api/v1/talks/1/",
            {
                "title": "Go",
                "description": "Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.",
                "start": "10:00:00",
            },
        )

    def test_put(self):
        """Put /api/v1/talks/1/ must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.resp.status_code)


class TalksDeleteValid(APITestCase):
    def setUp(self):
        Talk.objects.create(
            title="Rust",
            description="Uma linguagem capacitando todos a construir softwares confiáveis e eficientes.",
            start="08:00:00",
        )
        self.resp = self.client.delete("/api/v1/talks/1/")

    def test_delete(self):
        """Delete /api/v1/talks/1/ must return status code 204"""
        self.assertEqual(status.HTTP_204_NO_CONTENT, self.resp.status_code)
