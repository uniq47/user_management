from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'user_name': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'user_status': 'A',
            'department': 'IT'
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        user_data = {
            'user_name': 'test_api_user',
            'first_name': 'Test API',
            'last_name': 'User',
            'email': 'test@example.com',
            'user_status': 'A',
            'department': 'IT'
        }
        response = self.client.post(reverse('user-list-create'), user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Check if a new user is created

    def test_retrieve_user(self):
        response = self.client.get(reverse('user-detail', args=[self.user.user_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_name'], self.user.user_name)

    def test_update_user(self):
        updated_data = {
            'user_name': 'updated_user_name',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'user_status': 'T',
            'department': 'Finance'
        }
        response = self.client.put(reverse('user-detail', args=[self.user.user_id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.user_name, updated_data['user_name'])

    def test_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.user_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)