class Sensor:
    def __init__(self):
        self._threshold = 10

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        if value < 0:
            raise ValueError("Threshold must be non-negative")
        self._threshold = value

s = Sensor()
s.threshold = 0
print(s.threshold)  # Output: 15
