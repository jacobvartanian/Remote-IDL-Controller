import requests
import json

SERVER = "iot.nortcele.win"
PORT = "8080"

HTTP_STATUS_SUCCESS = 200

class Remote():
    def __init__(self, token, server = SERVER, port = PORT):
        self._server = server
        self._port = port
        self._token = token

    def publish(self, pin, value):
        url = "http://{0}:{1}/{2}/update/{3}?value={4}".format(self._server, self._port, self._token, pin, value)
        print(url)
        if requests.get(url).status_code == HTTP_STATUS_SUCCESS:
            return True
        return False

    def subscribe(self, pin):
        url = "http://{0}:{1}/{2}/get/{3}".format(self._server, self._port, self._token, pin)
        value = None
        data = requests.get(url)
        if data.status_code == HTTP_STATUS_SUCCESS:
            value = json.loads(data.content)
        return value
