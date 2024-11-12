from Adder4bit import Adder4bit


class Adder16bit:
    def __init__(self, a: str, b: str, carry_in: str):
        if len(a) != 16 or len(b) != 16 or len(carry_in) != 1:
            raise TypeError("Adder16bit: Invalid type")
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__output = None
        self.__carry_out = 0
        self.__execute()
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("Adder16bit: Invalid operation")
        return str(self.__output)[::-1]
    
    
    def get_carry_out(self) -> str:
        return str(self.__carry_out)
    
    
    def __execute(self):
        for i in range(15, -1, -4):
            a = self.__a[i - 3:i + 1]
            b = self.__b[i - 3:i + 1]
            carry_in = self.__carry_in
            adder = Adder4bit(a, b, carry_in)
            self.__output += adder.get_output()[::-1]
            self.__carry_in = adder.get_carry_out()