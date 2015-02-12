from django.contrib.auth.models import User
from django.test import TestCase, Client

from apps.tickets.models import Ticket


class FW2TicketsTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='user', password='user')
        User.objects.create_user(username='noticket', password='noticket')

        new_ticket = Ticket(author=User.objects.get(pk=1), title='test ticket title', message='test ticket message')
        new_ticket.save()

        self.client = Client()

    def test_anonymous_user_tickets(self):
        """
        Try to access multiple pages as an AnonymousUser
        """

        response = self.client.get('/tickets/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/tickets/new/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

        response = self.client.get('/tickets/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')

    def test_user_owning_tickets(self):
        """
        Try to access multiple pages as a simple user
        """

        response = self.client.login(username='user', password='user')
        self.assertEqual(response, True)

        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/tickets/new/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/tickets/1/')
        self.assertEqual(response.status_code, 200)

    def test_user_without_tickets(self):
        """
        Try to access a ticket not owned by user.
        """

        response = self.client.login(username='noticket', password='noticket')
        self.assertEqual(response, True)

        response = self.client.get('/tickets/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/tickets/new/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/tickets/1/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='')