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
        print("try to ping all")
        for northlamps in self.config["lamps"]["north"]:
            try:
                requests.post("http://" + self.config["lamps"]["south"][northlamps] + ":8080/signal",
                              data=None,
                              json=self.config["signal"],
                              headers={'Content-Type': 'application/json'}
                              )

            except:
                print("ping all failed to ping " + northlamps)
        for southlamps in self.config["lamps"]["south"]:
            try:

                requests.post("http://" + self.config["lamps"]["south"][southlamps] + ":8080/signal",
                              data=None,
                              json=self.config["signal"],
                              headers={'Content-Type': 'application/json'}
                              )
            except:
                print("ping all failed to ping " + southlamps)

    def get_direction(self, post):
        print("estimate direction")
        for northlamps in self.config["lamps"]["north"]:
            if self.config["lamps"]["south"][northlamps] == post["sender"]:
                print("north")
                self.direction = "north"
        for southlamps in self.config["lamps"]["south"]:
            if self.config["lamps"]["south"][southlamps] == post["sender"]:
                print("south")
                self.direction = "south"

    def ping_to_direction(self):
        print("try to ping into direction")
        for lamps in self.config["lamps"][self.direction]:
            try:
                requests.post("http://" + self.config["lamps"][self.direction][lamps] + ":8080/signal",
                              data=None,
                              json={
                                  "counter": 0,
                                  "url": self.config["signal"]["url"]
                              },
                              headers={'Content-Type': 'application/json'}
                              )
            except:
                print("failed to ping into direction")

    def use_signal(self):
        print("try to use signal")
        if self.standby:
            print("is on standby")
            self.ping_to_direction()
            self.lamp().ligth_on()

        else:
            print("not on standby")
            self.ping_all()
