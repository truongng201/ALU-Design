from Adder1bit import Adder1bit


class Adder4bit:
    def __init__(self, a: str, b: str, carry_in: str):
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__s = None
        self.__carry_out = 0
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if len(self.__a) != 4 or len(self.__b) != 4 or len(self.__carry_in) != 1:
            raise TypeError("Adder4bit: Invalid type")
        for i in range(4):
            if self.__a[i] not in ("0", "1") or self.__b[i] not in ("0", "1") or self.__carry_in not in ("0", "1"):
                raise TypeError("Adder4bit: Invalid type")
    
    
    def get_s(self) -> str:
        if self.__s == None:
            raise ValueError("Adder4bit: Invalid operation")
        return str(self.__s)[::-1]
    
    
    def get_carry_out(self) -> str:
        return str(self.__carry_out)
    
    
    def __execute(self):
        for i in range(3, -1, -1):
            a = self.__a[i]
            b = self.__b[i]
            carry_in = self.__carry_in
            adder = Adder1bit(a, b, carry_in)
            self.__s += adder.get_s()
            self.__carry_in = adder.get_carry_out()
        self.__carry_out = self.__carry_in
    
    