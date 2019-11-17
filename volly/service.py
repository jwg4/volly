import requests

DEFAULT_URL = "https://volatile.wtf"


class Service(object):
    def __init__(self, url=DEFAULT_URL):
        self.base_url = url

    def store(self, key, value):
        pass

    def retrieve(self, key):
        url = "%s/%s" % (self.base_url, key)
        r = requests.get(url)
        return r.content

    def __setitem__(self, key, value):
        self.store(key, value)

    def __getitem__(self, key):
        return self.retrieve(key)
