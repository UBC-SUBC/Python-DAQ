from importlib import import_module

class Depth_Sensor:
    
    def __init__(self) -> None:
        self.ms5837 = import_module("ms5837")
        self.sensor = self.ms5837.MS5837_02BA(1)
        self.sensor.init()
    
    
    def outputDict(self):
        freshwaterDepth = self.sensor.depth() # default is freshwater
        self.sensor.setFluidDensity(self.ms5837.DENSITY_SALTWATER)
        saltwaterDepth = self.sensor.depth() # No nead to read() again
        self.sensor.setFluidDensity(1000) # kg/m^3
        print(("Depth: %.3f m (freshwater)  %.3f m (saltwater)") % (freshwaterDepth, saltwaterDepth))
        print("ATM:",  self.sensor.pressure(self.ms5837.UNITS_atm))
        
        return {
            'fresh_depth': freshwaterDepth,
            'salt_depth': saltwaterDepth
        }
        
        
        
        
class Dummy_Depth_Sensor:
    def outputDict(self):
        return {
            'fresh_depth': -9999,
            'salt_depth': -9999
        }