from unittest import TestCase

from volly import Service


class TestService(TestCase):
    def test_init(self):
        svc = Service("http://www.example.com")
        self.assertIsNotNone(svc)

    def test_read_and_write(self):
        svc = Service("http://www.example.com")
        svc["ZFHIAUNGYI"] = "P3XD8NWG7K"
        self.assertEqual(svc["ZFHIAUNGYI"], "P3XD8NWG7K")