from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use home.html"""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_subscription_link(self):
        """Must have a link to home"""
        expected = 'href="{}"'.format(r('home'))
        self.assertContains(self.response, expected)
