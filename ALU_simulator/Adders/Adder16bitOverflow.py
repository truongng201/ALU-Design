from Adder4bitOverflow import Adder4bitOverflow
from Adder4bit import Adder4bit


class Adder16bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 16 or len(b) != 16 or len(carry_in) != 1:
            raise TypeError("Adder16bitOverflow: Invalid type")
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
        for i in range(15, -1, -4):
            a = self.__a[i - 3:i + 1]
            b = self.__b[i - 3:i + 1]
            carry_in = self.__carry_in
            if i != 3:
                adder = Adder4bit(a, b, carry_in)
                self.__s += adder.get_s()[::-1]
                self.__carry_in = adder.get_carry_out()
            else:
                adder = Adder4bitOverflow(a, b, carry_in)
                self.__s += adder.get_s()[::-1]
                self.__overflow = int(adder.get_overflow())