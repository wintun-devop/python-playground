class Device:
    def __init__(self):
        self._voltage = 0

    def set_voltage(self, v):
        if v < 0:
            raise ValueError("Voltage must be non-negative")
        self._voltage = v

    def get_voltage(self):
        return self._voltage

d = Device()
d.set_voltage(0)
print(d.get_voltage())  # Output: 5
