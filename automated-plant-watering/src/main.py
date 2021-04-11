import time

import network

from Config import Config
from MoistureSensor import MoistureSensor

import blynklib_mp as blynk

from Pump import Pump


def connect_to_wifi():
    WIFI_SSID = 'Gliwice test 5G 300% mocy'
    WIFI_PASS = 'Kebab218mieszany'
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)

    # check if board connected
    connect_status = wifi.isconnected()
    print("Wifi connection result: " + str(connect_status))

connect_to_wifi()

CONFIG_PATH = "configuration\\config.json"
config = Config(CONFIG_PATH)
blynk = blynk.Blynk(config.get_blynk_auth_token())

air_value = 3620
water_value = 1360
minimum_soil_moisture_percentage = 30

moisture_sensor_34 = MoistureSensor(pin_number=34,
                                    air_value=air_value,
                                    water_value=water_value)

moisture_sensor_35 = MoistureSensor(pin_number=35,
                                    air_value=air_value,
                                    water_value=water_value)

moisture_sensor_32 = MoistureSensor(pin_number=32,
                                    air_value=air_value,
                                    water_value=water_value)

moisture_sensor_33 = MoistureSensor(pin_number=33,
                                    air_value=air_value,
                                    water_value=water_value)

pump_x = Pump(duration=10, pin_out=10)
pump_y = Pump(duration=10, pin_out=10)
pump_z = Pump(duration=10, pin_out=10)
pump_zz = Pump(duration=10, pin_out=10)

moisture_sensors = [(moisture_sensor_34, pump_x),
                    (moisture_sensor_35, pump_y),
                    (moisture_sensor_32, pump_z),
                    (moisture_sensor_33, pump_zz)]



# moisutre sensors
@blynk.handle_event('read V1')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, moisture_sensor_34.read_value())


@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, moisture_sensor_35.read_value())


@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, moisture_sensor_32.read_value())


@blynk.handle_event('read V4')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, moisture_sensor_33.read_value())


# is blocked indicators
@blynk.handle_event('read V9')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, pump_x.watered_last_1h()*1)


@blynk.handle_event('read V10')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, pump_y.watered_last_1h()*1)


@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, pump_z.watered_last_1h()*1)


@blynk.handle_event('read V12')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin, pump_zz.watered_last_1h()*1)


while True:

    for sensor, pump in moisture_sensors:
        value = sensor.read_value()
        if value < minimum_soil_moisture_percentage:
            pump.start_pump()

    blynk.run()
    time.sleep_ms(500)
