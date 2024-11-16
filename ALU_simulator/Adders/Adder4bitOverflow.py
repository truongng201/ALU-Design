from Adder1bit import Adder1bit
from utils import InvalidType, InvalidOperation, BIT_VALUE


class Adder4bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        self.__BIT_LENGTH = 4
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__output = None
        self.__overflow = 0
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if len(self.__a) != self.__BIT_LENGTH or len(self.__b) != self.__BIT_LENGTH:
            raise InvalidType("Adder4bitOverflow")
        for i in range(self.__BIT_LENGTH):
            if self.__a[i] not in BIT_VALUE or self.__b[i] not in BIT_VALUE:
                raise InvalidType("Adder4bitOverflow")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("Adder4bitOverflow")
    
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise InvalidOperation("Adder4bitOverflow")
        return str(self.__output)
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def __execute(self):
        for i in range(self.__BIT_LENGTH - 1, -1, -1):
            a = self.__a[i]
            b = self.__b[i]
            carry_in = self.__carry_in
            adder = Adder1bit(a, b, carry_in)
            self.__output += adder.get_output()
            self.__carry_in = adder.get_carry_out()
            if i == 1:
                self.__overflow = int(self.__carry_in)
            elif i == 0:
                self.__overflow ^= int(self.__carry_in)
        self.__output = str(self.__output)[::-1]
