from datetime import time


class Lamp:
    def __init__(self):
        self.ligth = False

    def let_it_glow(self):
        set.ligth = True
        time.sleep(15)
        set.ligth = False

    def start_thread(self):
        # x = threading.Thread(target=)
        pass
