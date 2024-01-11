from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Command, User

"""
Tests for Command.
"""


class CommandViewSetTestCase(APITestCase):
    def setUp(self):
        try:
            self.command_data_main = {'name': 'test_command'}
            self.command = Command.objects.create(**self.command_data_main)
            self.url = 'http://127.0.0.1:8000/command/'
        except AssertionError as e:
            print(f'Test setUp for command failed: {str(e)}')

    def test_create_command(self):
        self.command_data = {'name': 'test_command_2'}
        response = self.client.post(self.url, self.command_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=f'Create command should return 201 status code. Error: {response.content}')

    def test_retrieve_command(self):
        response = self.client.get(reverse('command-detail', args=[self.command.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Retrieve command should return 200 status code. Error: {response.content}')

    def test_update_command(self):
        updated_data = {'name': 'UpdatedName'}
        response = self.client.put(reverse('command-detail', args=[self.command.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Update command should return 200 status code. Error: {response.content}')

    def test_delete_command(self):
        response = self.client.delete(reverse('command-detail', args=[self.command.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         msg=f'Delete command should return 204 status code. Error: {response.content}')


"""
Tests for User.
"""


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        try:
            self.user_data_main = {'name': 'Rachel', 'surname': 'Green', 'mail': 'rachelgreen@example.com'}
            self.user = User.objects.create(**self.user_data_main)
            self.url = 'http://127.0.0.1:8000/user/'
        except AssertionError as e:
            print(f'Test setUp for user failed: {str(e)}')

    def test_create_user(self):
        self.user_data = {'name': 'Monica', 'surname': 'Geller', 'mail': 'monicageller@example.com'}
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=f'Create user should return 201 status code. Error: {response.content}')

    def test_retrieve_user(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Retrieve user should return 200 status code. Error: {response.content}')

    def test_update_user(self):
        updated_data = {'name': 'UpdatedName', 'surname': self.user.surname, 'mail': self.user.mail}
        response = self.client.put(reverse('user-detail', args=[self.user.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Update user should return 200 status code. Error: {response.content}')

    def test_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         msg=f'Delete user should return 204 status code. Error: {response.content}')
