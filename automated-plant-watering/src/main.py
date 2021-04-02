import time

from sensors.MoistureSensor import MoistureSensor

if __name__ == "__main__":
    air_value = 3620
    water_value = 1360

    moisture_sensor_34 = MoistureSensor(pin_number=34,
                                        air_value=air_value,
                                        water_value=water_value)

    moisture_sensor_35 = MoistureSensor(pin_number=35,
                                        air_value=air_value,
                                        water_value=water_value)

    while True:
        m_s_34_value = moisture_sensor_34.read_value()

        print("pin34: " + str(m_s_34_value))

        m_s_35_value = moisture_sensor_35.read_value()

        print("pin35: " + str(m_s_35_value))
        time.sleep_ms(500)
