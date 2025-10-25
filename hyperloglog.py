# hyperloglog.py
import mmh3
import math

class HyperLogLog:
    def __init__(self, p=14):
        self.p = p
        self.m = 1 << p  # Number of registers
        self.registers = [0] * self.m  # Registers
        self.alpha = self._get_alpha()
        self.small_range_correction = 5 * self.m / 2  # Correction for small values

    def _get_alpha(self):
        """Returns the alpha correction value based on p."""
        if self.p <= 16:
            return 0.673
        elif self.p == 32:
            return 0.697
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, item):
        """Adds an item to the HyperLogLog estimator."""
        x = mmh3.hash(str(item), signed=False)
        j = x & (self.m - 1)  # Register index
        w = x >> self.p  # Hash value
        self.registers[j] = max(self.registers[j], self._rho(w))  # Update register

    def _rho(self, w):
        """Returns the rank (leading zero count) of the hash value."""
        return len(bin(w)) - 2 if w > 0 else 32

    def count(self):
        """Estimates the cardinality of the data."""
        Z = sum(2.0 ** -r for r in self.registers)
        E = self.alpha * self.m * self.m / Z
        
        if E <= self.small_range_correction:
            V = self.registers.count(0)
            if V > 0:
                return self.m * math.log(self.m / V)
        
        return E
