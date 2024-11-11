from Adder1bit import Adder1bit

class Adder4bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 4 or len(b) != 4 or len(carry_in) != 1:
            raise TypeError("Adder4bitOverflow: Invalid type")
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
        for i in range(3, -1, -1):
            a = self.a[i]
            b = self.b[i]
            carry_in = self.carry_in
            adder = Adder1bit(a, b, carry_in)
            self._s += adder.get_s()
            self.carry_in = adder.get_carry_out()
            if i == 1:
                self._overflow = int(self.carry_in)
            elif i == 0:
                self._overflow ^= int(self.carry_in)
            