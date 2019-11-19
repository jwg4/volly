class HTTPResponseException(Exception):
    def __init__(self, service, key):
        self.service = service
        self.key = key


class MissingKeyException(HTTPResponseException):
    pass


def Error(response, service, key):
    if response.status_code == 404:
        return MissingKeyException(service, key)
    else:
        return HTTPResponseException(service, key)
