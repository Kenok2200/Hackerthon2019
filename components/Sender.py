class Sender:

    def __init__(self, config):
        self.config = config

    def send_signal_on_all(self):
        for northlamps in self.json_of_lamps["north"]:
            print(northlamps)
        for southlamps in self.json_of_lamps["south"]:
            print(southlamps)
