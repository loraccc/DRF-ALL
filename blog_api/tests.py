from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
# Create your tests here.


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_api:listcreate' )
        response = self.client.get(url , format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)