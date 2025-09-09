class Sensor:
    def __init__(self):
        self.temperature:float = 22.5
        self.humidity:int = 60

my_sensor = Sensor()

# Access attribute dynamically(getter)
value = getattr(my_sensor, "temperature","Not Exist")
print(value) 

# With default fallback
missing = getattr(my_sensor, "pressure", "Not available")
print(missing)

setattr(my_sensor,"temperature",40)
print(my_sensor.temperature)

my_hasattr_test = hasattr(my_sensor,"temperature")
print("test",my_hasattr_test)

my_delattr_test = delattr(my_sensor,"temperature")
print("test",my_delattr_test)
# print("test",my_sensor.temperature)
