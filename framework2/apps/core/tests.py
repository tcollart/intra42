from django.contrib.auth.models import User
from django.test import TestCase, Client


class FW2CoreTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='user', password='user')
        User.objects.create_superuser(username='admin', email=None, password='admin')
        self.client = Client()

    def test_anonymous_user_connection(self):
        """
        Try to access multiple pages as an AnonymousUser
        """

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.login(username='fake', password='fake')
        self.assertEqual(response, False)

        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

    def test_simple_user_connection(self):
        """
        Try to access multiple pages as a simple user
        """

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.login(username='user', password='user')
        self.assertEqual(response, True)

        response = self.client.get('/signup/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/signin/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')