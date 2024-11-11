from Adder4bit import Adder4bit
from Adder4bitOverflow import Adder4bitOverflow

class Adder16bit:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 16 or len(b) != 16 or len(carry_in) != 1:
            raise TypeError("Adder16bit: Invalid type")
        self.a = a
        self.b = b
        self.carry_in = carry_in
        self._s = ""
        self._carry_out = 0
        self._run()
        
    
    def get_s(self) -> str:
        return str(self._s)[::-1]
    
    
    def get_carry_out(self) -> str:
        return str(self._carry_out)
    
    
    def _run(self):
        for i in range(15, -1, -4):
            a = self.a[i - 4:i]
            b = self.b[i - 4:i]
            carry_in = self.carry_in
            adder = Adder4bit(a, b, carry_in)
            self._s += adder.get_s()[::-1]
            self.carry_in = adder.get_carry_out()