from django.test import TestCase, Client
from django.contrib.auth.models import User


class Framework1TestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='user', password='user')
        User.objects.create_superuser(username='admin', email=None, password='admin')
        self.client = Client()

    def test_anonymous_user_connection(self):
        """
        Anonymous user:
            - Access sign out page with an AnonymousUser
            - Access sign in page logging in User
            - Access sign up page while logged in
            - Access admin page as simple user
            - Access sign in page while logged in
            - Delete an user
        """

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.login(username='fake', password='fake')
        self.assertEqual(response, False)

        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/')
        self.assertRedirects(response, '/admin/user/', status_code=301, target_status_code=302, msg_prefix='')

        response = self.client.get('/admin/user/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/create/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/delete/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.post('/admin/user/delete/1/', {'pk': '1'})
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        user = User.objects.filter(pk=1)
        self.assertEqual(len(user), 1)

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

    def test_simple_user_connection(self):
        """
        Simple user:
            - Access sign out page with an AnonymousUser
            - Access sign in page logging in User
            - Access sign up page while logged in
            - Access admin page as simple user
            - Access sign in page while logged in
            - Delete an user
        """

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.login(username='user', password='user')
        self.assertEqual(response, True)

        response = self.client.get('/signup/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/signin/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/')
        self.assertRedirects(response, '/admin/user/', status_code=301, target_status_code=302, msg_prefix='')

        response = self.client.get('/admin/user/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/create/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/delete/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.post('/admin/user/delete/1/', {'pk': '1'})
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        user = User.objects.filter(pk=1)
        self.assertEqual(len(user), 1)

        response = self.client.get('/signout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

    def test_staff_user_connection(self):
        """
        Staff user:
            - Access admin pages as staff user
            - Delete an user
        """

        response = self.client.login(username='admin', password='admin')
        self.assertEqual(response, True)

        response = self.client.get('/admin/')
        self.assertRedirects(response, '/admin/user/', status_code=301, target_status_code=200, msg_prefix='')

        response = self.client.get('/admin/user/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/user/create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/user/1/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/user/delete/1/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/admin/user/delete/2/', {'pk': '2'})
        self.assertRedirects(response, '/admin/user/', status_code=302, target_status_code=302, msg_prefix='')

        user = User.objects.filter(pk=2)
        self.assertEqual(len(user), 0)