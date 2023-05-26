# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board 
import adafruit_bno055 
import RPi.GPIO as GPIO 
import time

# Set Up GPIO Pins
# GPIO.setmode(GPIO.BOARD)
#Set GPIO_4 (Controls RST) and GPIO_14 (Controls INT) as Outputs 
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

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
        
    #Reset Absolute Orientation Sensor!
    def RST_BNO055(self): # toggles GPIO_4 (RPi) --> RST(BNO055)
        #Hardware reset pin.  Set this pin low then high to cause a reset on the sensor. 
        GPIO.output(4,GPIO.LOW)
        #Delay by 1 second
        time.sleep(1)
        GPIO.output(4,GPIO.HIGH) 
        print("~Reset Executed~")






    