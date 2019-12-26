import requests

DOMAIN = "iot.nortcele.win"
PORT = "8080"

class Remote():
    def __init__(self, token, domain = DOMAIN, port = PORT):
        self._domain = domain
        self._port = port
        self._token = token

    def publish(self, pin, value):
        url = "http://{0}:{1}/{2}/update/{3}?value={4}".format(self._domain, self._port, self._token, pin, value)
        print(url)
        # requests.get(url)
        #TODO get a valid return
        return True