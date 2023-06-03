from importlib import import_module

class Depth_Sensor:
    
    def __init__(self) -> None:
        self.SMbus = import_module("smbus2.SMBus")
    
    

class Dummy_Depth_Sensor:
    