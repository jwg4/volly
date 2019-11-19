from unittest import TestCase

from volly import Service
from volly.error import MissingKeyException


class TestService(TestCase):
    def test_init(self):
        svc = Service("http://www.example.com")
        self.assertIsNotNone(svc)

    def test_read_and_write(self):
        svc = Service("https://volatile.wtf")
        svc["ZFHIAUNGYI"] = "P3XD8NWG7K"
        self.assertEqual(svc["ZFHIAUNGYI"], b'P3XD8NWG7K')

    def test_write_missing_value(self):
        svc = Service("https://volatile.wtf")
        self.assertRaises(lambda: svc["UNGYIZFHIA"], MissingKeyException)
