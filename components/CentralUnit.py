import json

import requests

from components.Lamp import Lamp
from components.Receiver import Receiver
from components.Sender import Sender
from components.Sensor import Sensor


class CentralUnit:

    def __init__(self):
        self.config = self.load_config_file("config.json")
        self.sender = Sender(self.config["lamps"])
        self.sensor = Sensor(self.config["raspberry"]["echo"], self.config["raspberry"]["trigger"])
        self.lamp = Lamp
        self.receiver = Receiver
        self.standby = False
        self.direction = ""

    def log(message, level):
        print(level + ": " + message)

    @staticmethod  # static method as this method has to be reachable before Object initiation
    def load_config_file(filepath):
        with open(filepath, 'r') as config_file:
            return json.load(config_file)

    def ping_all(self):
        for northlamps in self.config["lamps"]["north"]:
            requests.post(northlamps + "/signal",
                          data=None,
                          json=self.config["counter"],
                          headers={'Content-Type': 'application/json'}
                          )
        for southlamps in self.config["lamps"]["south"]:
            requests.post(southlamps + "/signal",
                          data=None,
                          json=self.config["counter"],
                          headers={'Content-Type': 'application/json'}
                          )

    def get_direction(self, post):
        for northlamps in self.config["lamps"]["north"]:
            if northlamps == post["sender"]:
                self.direction = "north"
        for southlamps in self.config["lamps"]["south"]:
            if southlamps == post["sender"]:
                self.direction = "south"

    def ping_to_direction(self):
        for lamps in self.config["lamps"][self.direction]:
            requests.post(lamps + "/signal",
                          data=None,
                          json={
                              "counter": 0,
                              "url": self.config["signal"]["url"]
                          },
                          headers={'Content-Type': 'application/json'}
                          )

    def ligth_up(self):
        self.lamp.ligth_on()

    def use_signal(self, post):
        if self.standby:

            self.ping_to_directon
            self.ligth_up

        else:
            self.ping_all()
