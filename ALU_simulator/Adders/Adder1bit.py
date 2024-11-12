class Adder1bit:
    def __init__(self, a: str, b: str, carry_in: str):
        self.__a = int(a)
        self.__b = int(b)
        self.__carry_in = int(carry_in)
        self.__output = None
        self.__carry_out = 0
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if self.__a not in (0, 1) or self.__b not in (0, 1) or self.__carry_in not in (0, 1):
            raise TypeError("Adder1bit: Invalid type")
    
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("Adder1bit: Invalid operation")
        return str(self.__output)
    
    
    def get_carry_out(self) -> str:
        return str(self.__carry_out)
    
    
    def __execute(self):
        self.__output = (self.__a ^ self.__b) ^ self.__carry_in
        self.__carry_out = (self.__a and self.__carry_in) or (self.__b and self.__carry_in) or (self.__a and self.__b)