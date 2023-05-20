# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board 
import adafruit_bno055 
import RPi.GPIO as GPIO 
import time


#from adafruit_extended_bus import ExtendedI2C as I2C

class IMU_module:
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    last_val = 0xFFFF
    
    def temperature(self):
        global last_val  # pylint: disable=global-statement
        result = self.sensor.temperature
        if abs(result - self.last_val) == 128:
            result = self.sensor.temperature
            if abs(result - self.last_val) == 128:
                return 0b00111111 & result
        last_val = result
        return result

    def outputDict(self):
        return {
            "temperature": self.temperature(),
            "acceleration": self.sensor.acceleration,
            "magnetic": self.sensor.magnetic,
            "gyro": self.sensor.gyro,
            "euler": self.sensor.euler,
            "quaternion": self.sensor.quaternion,
            "linear_acceleration": self.sensor.linear_acceleration,
            "gravity": self.sensor.gravity
        }
    
    
        


    
# while True:
#     # print("Temperature: {} degrees C".format(sensor.temperature))
    
#     print(
#         "Temperature: {} degrees C".format(temperature())
#     )  # Uncomment if using a Raspberry Pi
    
#     print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#     print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#     print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#     print("Euler angle: {}".format(sensor.euler))
#     print("Quaternion: {}".format(sensor.quaternion))
#     print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
#     print("Gravity (m/s^2): {}".format(sensor.gravity))
#     print()

    # time.sleep(1)
    