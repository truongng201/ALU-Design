from Adder16bitOverflow import Adder16bitOverflow
from Adder16bit import Adder16bit


class Adder32bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 32 or len(b) != 32 or len(carry_in) != 1:
            raise TypeError("Adder32bitOverflow: Invalid type")
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__s = ""
        self.__overflow = 0
        self.__execute()
        
    
    def get_s(self) -> str:
        return str(self.__s)[::-1]
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def __execute(self):
        for i in range(31, -1, -16):
            a = self.__a[i - 15:i + 1]
            b = self.__b[i - 15:i + 1]
            carry_in = self.__carry_in
            if i != 15:
                adder = Adder16bit(a, b, carry_in)
                self.__s += adder.get_s()[::-1]
                self.__carry_in = adder.get_carry_out()
            else:
                adder = Adder16bitOverflow(a, b, carry_in)
                self.__s += adder.get_s()[::-1]
                self.__overflow = int(adder.get_overflow())
                