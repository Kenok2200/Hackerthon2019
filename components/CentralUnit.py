import json

from components.Lamp import Lamp
from components.Receiver import Receiver
from components.Sender import Sender
from components.Sensor import Sensor


class CentralUnit:

    def __init__(self):
        self.lamp = Lamp
        self.receiver = Receiver
        self.sensor = Sensor
        self.config = self.load_config_file("config.json")
        self.sender = Sender(self.config["lamps"])

    def log(message, level):
        print(level + ": " + message)

    @staticmethod  # static method as this method has to be reachable before Object initiation
    def load_config_file(filepath):
        with open(filepath, 'r') as config_file:
            return json.load(config_file)


def main():
    print("start")
    central_unit = CentralUnit()
    # TODO Here happens the Magic
    pass


if __name__ == '__main__':
    main()
