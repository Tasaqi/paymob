from django.test import TestCase
from urllib.parse import urljoin
from paymob import  settings


class ViewsTestCase(TestCase):

    def test_first_view(self):
        response = self.client.get(settings.TESTING_ROOT_URL)
        # test case:  first view is live
        self.assertEqual(response.status_code, 200)
        # test case: the drop down have greater than one key
        self.assertTrue(len(response.context.get("keys")) > 0)

    def test_second_view(self):
        response = self.client.get(settings.TESTING_ROOT_URL)
        # test case:  first view is live
        self.assertEqual(response.status_code, 200)

    def test_second_empty_response(self):
        payload = "second?key="
        response = self.client.get(urljoin(settings.TESTING_ROOT_URL, payload))
        matches = response.context.get("matches")
        self.assertEqual(matches, None)

    def test_second_view_with_a_key(self):
        payload = "second?key=ALCURONIUM CHLORIDE 5MG/ML 2ML INJECTION"
        response = self.client.get(urljoin(settings.TESTING_ROOT_URL, payload))
        matches = response.context.get("matches")
        self.assertTrue(len(matches) > 0)