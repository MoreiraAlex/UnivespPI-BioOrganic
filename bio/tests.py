from django.test import TestCase
from django.urls import reverse, resolve

pattern_name = 'bio:home'

class TestBioViews(TestCase):

    def test_reverse(self):
        self.assertEqual(reverse(pattern_name), '/')

    def test_resolve(self):
        self.assertEqual(resolve('/').view_name, pattern_name)

    def test_status_code(self):
        response = self.client.get(reverse(pattern_name))
        self.assertEqual(response.status_code, 200)

