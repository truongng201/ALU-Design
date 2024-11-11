class Adder1bit:
    def __init__(self, a: int, b: int, carry_in: int) -> None:
        if a not in (0, 1) or b not in (0, 1) or carry_in not in (0, 1):
            raise TypeError("Invalid type")
        self.a = a
        self.b = b
        self.carry_in = carry_in
        self._s  = None
        self._carry_out = 0
        self._set_carry_out()
        self._set_s()
    
    
    def _set_s(self):
        self._s = (self.a ^ self.b) ^ self.carry_in
        
    
    def _set_carry_out(self):
        self._carry_out = (self.a and self.carry_in) or (self.b and self.carry_in) or (self.a and self.b)
    
    
    def get_s(self):
        return self._s
    
    
    def get_carry_out(self):
        return self._carry_out