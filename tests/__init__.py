from unittest import TestCase

from volly import Service


class TestService(TestCase):
    def test_init(self):
        svc = Service("http://www.example.com")
        self.assertIsNotNone(svc)
