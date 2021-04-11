from machine import Pin, ADC
from SensorBase import SensorBase


class MoistureSensor(SensorBase):

    def __init__(self, pin_number, air_value, water_value):
        self.pin34 = ADC(Pin(pin_number))
        self.pin34.atten(ADC.ATTN_11DB)
        self.air_value = air_value  # max
        self.water_value = water_value  # min

    def read_value(self):
        value = self.pin34.read()
        percentage_value = self.convert_to_percentage_inverted(self.water_value, self.air_value, value)
        return percentage_value

    def write_value(self):
        pass

    def convert_to_percentage_inverted(self, min, max, value):
        offset_less_value = value - min
        offset_less_max = max - min
        if offset_less_max <= 0:
            print("ERROR: while converting to percentage, max is less than min")
            raise ValueError("ERROR: while converting to percentage, max is less than min")
        if offset_less_value < 0:
            offset_less_value = 0
            # print("WARNING: while converting to percentage, value is less than minimum value")
        return (1 - (offset_less_value / offset_less_max)) * 100

