from Adder4bitOverflow import Adder4bitOverflow
from Adder4bit import Adder4bit


class Adder16bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 16 or len(b) != 16 or len(carry_in) != 1:
            raise TypeError("Adder16bitOverflow: Invalid type")
        self.a = a
        self.b = b
        self.carry_in = carry_in
        self._s = ""
        self._overflow = 0
        self._run()
        
    
    def get_s(self) -> str:
        return str(self._s)[::-1]
    
    
    def get_overflow(self) -> str:
        return str(self._overflow)
    
    
    def _run(self):
        for i in range(15, -1, -4):
            a = self.a[i - 3:i + 1]
            b = self.b[i - 3:i + 1]
            carry_in = self.carry_in
            if i != 3:
                adder = Adder4bit(a, b, carry_in)
                self._s += adder.get_s()[::-1]
                self.carry_in = adder.get_carry_out()
            else:
                adder = Adder4bitOverflow(a, b, carry_in)
                self._s += adder.get_s()[::-1]
                self._overflow = int(adder.get_overflow())