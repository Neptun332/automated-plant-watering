from machine import Pin
import time
from machine import Pin, ADC
import time

def convert_to_percentage_inverted(min, max, value):
    offset_less_value = value - min
    offset_less_max = max - min
    if offset_less_max <= 0:
        print("ERROR: while converting to percentage, max is less than min")
        raise ValueError
    if offset_less_value < 0:
        offset_less_value = 0
        print("WARNING: while converting to percentage, value is less than minimum value")
    return (1 - (offset_less_value/offset_less_max))*100





if __name__ == "__main__":
    air_value = 3620
    water_value = 1360

    pin34 = ADC(Pin(34))
    pin34.atten(ADC.ATTN_11DB)

    pin35 = ADC(Pin(35))
    pin35.atten(ADC.ATTN_11DB)
    # Full range: 3.3v

    min_pin34 = 10000
    min_pin35 = 10000

    while True:
        pin34_value = pin34.read()
        if pin34_value < min_pin34:
            min_pin34 = pin34_value
        # pin34_value_percentage = convert_to_percentage_inverted(water_value, air_value, pin34_value)
        print("pin34: " + str(min_pin34))

        pin35_value = pin35.read()
        if pin35_value < min_pin35:
            min_pin35 = pin35_value
        # pin35_value_percentage = convert_to_percentage_inverted(water_value, air_value, pin35_value)
        print("pin35: " + str(min_pin35))
        time.sleep_ms(500)
