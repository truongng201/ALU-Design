class Adder1bit:
    def __init__(self, a: str, b: str, carry_in: str):
        if a not in ("0", "1") or b not in ("0", "1") or carry_in not in ("0", "1"):
            raise TypeError("Adder1bit: Invalid type")
        self.a = int(a)
        self.b = int(b)
        self.carry_in = int(carry_in)
        self._s = ""
        self._carry_out = 0
        self._set_carry_out()
        self._set_s()
    
    
    def _set_s(self):
        self._s = (self.a ^ self.b) ^ self.carry_in
        
    
    def _set_carry_out(self):
        self._carry_out = (self.a and self.carry_in) or (self.b and self.carry_in) or (self.a and self.b)
    
    
    def get_s(self) -> str:
        return str(self._s)
    
    
    def get_carry_out(self) -> str:
        return str(self._carry_out)