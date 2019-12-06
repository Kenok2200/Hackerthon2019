class Sensor():
    def __init__(self):
        self.json_of_lamps = {
            "north": {
                "1"
            },
            "south": {
                "2"
            }
        }

    def send_signal_on_all(self):
        for northlamps in self.json_of_lamps["north"]:
            print(northlamps)
        for southlamps in self.json_of_lamps["south"]:
            print(southlamps)
