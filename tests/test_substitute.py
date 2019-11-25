from unittest import TestCase

from volly.testing import TestService


class TestSubstituteService(TestCase):
    def test_init(self):
        svc = TestService("http://www.example.com")
        self.assertIsNotNone(svc)

    def test_read_and_write(self):
        svc = TestService("https://volatile.wtf")
        svc["ZFHIAUNGYI"] = "P3XD8NWG7K"
        self.assertEqual(svc["ZFHIAUNGYI"], b'P3XD8NWG7K')

    def test_write_missing_value(self):
        svc = TestService("https://volatile.wtf")
        self.assertRaises(MissingKeyException, lambda: svc["UNGYIZFHIA"])
