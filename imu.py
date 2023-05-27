# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT


from importlib import import_module
import time
# Set Up GPIO Pins
# GPIO.setmode(GPIO.BOARD)
#Set GPIO_4 (Controls RST) and GPIO_14 (Controls INT) as Outputs 
# GPIO.setup(4,GPIO.OUT)
# GPIO.setup(14,GPIO.OUT)

class IMU_module:
    board = None
    adafruit_bno055 = None
    GPIO = None
    
    def __init__(self) -> None:
        self.board = import_module("board")
        self.adafruit_bno055 = import_module("adafruit_bno055")
        self.GPIO = import_module("RPi.GPIO")
        
        self.reset_pin = 17
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.reset_pin, self.GPIO.OUT)
        self.GPIO.output(self.reset_pin, self.GPIO.HIGH)
        
        # import adafruit_bno055 
        # import RPi.GPIO as GPIO 
        
        self.is_dummy = False
        
        self.i2c = self.board.I2C()  # uses board.SCL and board.SDA
        # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
        self.sensor = self.adafruit_bno055.BNO055_I2C(self.i2c)
        self.last_val = 0xFFFF
        
        self.RST_BNO055()
    
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
        self.GPIO.output(self.reset_pin ,self.GPIO.LOW)
        #Delay by 1 second
        time.sleep(1)
        self.GPIO.output(self.reset_pin ,self.GPIO.HIGH) 
        # Cleanup GPIO resources
        self.GPIO.cleanup()
        print("~Reset Executed~")


class IMU_module_dummy:
        
    def outputDict(self):
        return {
            "temperature": 0,
            "acceleration": 0,
            "magnetic": 0,
            "gyro": 0,
            "euler": [0, 0, 0],
            "quaternion": 0,
            "linear_acceleration": 0,
            "gravity": 0,
        }


    