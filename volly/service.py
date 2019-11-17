import requests

DEFAULT_URL = "https://volatile.wtf"


class Service(object):
    def __init__(self, url=DEFAULT_URL):
        self.base_url = url

    def store(self, key, value):
        pass

    def __getitem__(self, key):
        url = "%s/%s" % (self.base_url, key)
        r = requests.get(url)
        return r.content
