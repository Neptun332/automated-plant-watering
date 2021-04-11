import time


class Pump:

    def __init__(self, duration, pin_out):
        self.duration = duration
        self.last_watering = 0

    def start_pump(self):
        if not self.watered_last_1h():
            print("Pump goes brrrrr")

    def watered_last_1h(self):
        return self.last_watering - time.ticks_ms() < 3600000


