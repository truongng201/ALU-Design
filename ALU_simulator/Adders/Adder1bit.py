from ALU_simulator.utils import InvalidType, BIT_VALUE

class Adder1bit:
    def __init__(self, a: str, b: str, carry_in: str):
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__output = ""
        self.__carry_out = 0
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if self.__a not in BIT_VALUE or self.__b not in BIT_VALUE or self.__carry_in not in BIT_VALUE:
            raise InvalidType("Adder1bit")
    
    
    def get_output(self) -> str:
        return str(self.__output)
    
    
    def get_carry_out(self) -> str:
        return str(self.__carry_out)
    
    
    def __execute(self):
        self.__a = int(self.__a)
        self.__b = int(self.__b)
        self.__carry_in = int(self.__carry_in)
        self.__output = (self.__a ^ self.__b) ^ self.__carry_in
        self.__carry_out = (self.__a & self.__carry_in) | (self.__b & self.__carry_in) | (self.__a & self.__b)