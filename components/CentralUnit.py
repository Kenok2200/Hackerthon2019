import json

from components.Sender import Sender


class CentralUnit:

    def __init__(self):
        self.receiver = 1
        self.sensor = 3
        self.config = self.load_config_file("config.json")
        self.sender = Sender(self.config["lamps"])

    def log(message, level):
        print(level + ": " + message)

    @staticmethod
    def load_config_file(filepath):
        with open(filepath, 'r') as config_file:
            return json.load(config_file)


def main():
    print("start")
    central_unit = CentralUnit()
    pass


if __name__ == '__main__':
    main()
