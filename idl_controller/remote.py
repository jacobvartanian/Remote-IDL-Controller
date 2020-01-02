import requests
import json

HTTP_STATUS_SUCCESS = 200

BLYNK_DATA_FILE = "blynk_data.json"

class Remote():
    def __init__(self):
        try:
            with open(BLYNK_DATA_FILE, "rb") as fp:
                blynk_data = json.load(fp)
            self._server = blynk_data["server"]
            self._port = blynk_data["port"]
            self._token = blynk_data["token"]
        except FileNotFoundError:
            print("ERROR: Blynk configuration file, \"{0}\" could not be found".format(BLYNK_DATA_FILE))
            exit(-1)

    def publish(self, pin, value):
        """Publishes a value to a virtual pin on the blynk server through a http request

        Keyword arguments:
        pin -- The virtual pin to publish to as a string
        value -- The value to publish to that virtual pin
        """
        url = "http://{0}:{1}/{2}/update/{3}?value={4}".format(self._server, self._port, self._token, pin, value)
        print(url)
        if requests.get(url).status_code == HTTP_STATUS_SUCCESS:
            return True
        return False

    def subscribe(self, pin):
        """Returns a value from a virtual pin

        Keyword arguments:
        pin -- The virtual pin to publish to as a string
        
        Returns: a JSON object returned from that virtual pin.
        """
        url = "http://{0}:{1}/{2}/get/{3}".format(self._server, self._port, self._token, pin)
        value = None
        data = requests.get(url)
        if data.status_code == HTTP_STATUS_SUCCESS:
            value = json.loads(data.content)
        return value
