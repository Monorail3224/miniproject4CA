from django.test import TestCase
from django.urls import reverse
from .models import Poll, Choice
from django.contrib.auth.models import User

class PollModelTestCase(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question='Test Poll')

    def test_poll_question(self):
        self.assertEqual(str(self.poll), 'Test Poll')

class PollDetailViewTestCase(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question='Test Poll')
        self.choice = Choice.objects.create(poll=self.poll, choice_text='Choice 1')
        self.url = reverse('poll_detail', args=(self.poll.id,))

    def test_poll_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Poll')
        self.assertContains(response, 'Choice 1')

    def test_poll_vote(self):
        response = self.client.post(self.url, {'choice': self.choice.id})
        self.assertEqual(response.status_code, 302)  # Redirect after voting
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)

class PollCreateViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('poll_create')

    def test_poll_create_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_poll_create_success(self):
        data = {'question': 'New Poll', 'choices': 'Choice 1, Choice 2'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Poll.objects.filter(question='New Poll').exists())

class PollEditViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.poll = Poll.objects.create(question='Old Poll')
        self.choice = Choice.objects.create(poll=self.poll, choice_text='Old Choice 1')
        self.url = reverse('poll_edit', args=(self.poll.id,))

    def test_poll_edit_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_poll_edit_success(self):
        data = {'question': 'Updated Poll', 'choices': 'Choice 1, Choice 2'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful edit
        self.poll.refresh_from_db()
        self.choice.refresh_from_db()
        self.assertEqual(self.poll.question, 'Updated Poll')
        self.assertEqual(self.choice.choice_text, 'Choice 1')
