from ALU_simulator.utils import InvalidType, BIT_VALUE

class Xnor:
    def __init__(self, number_of_bit: int, input_a: str, input_b: str) -> None:
        self.__output = ""
        self.__number_of_bit = number_of_bit
        self.__input_a = input_a
        self.__input_b = input_b
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if len(self.__input_a) != len(self.__input_b):
            raise InvalidType("Xnor")
        if self.__number_of_bit != len(self.__input_a):
            raise InvalidType("Xnor")
        if self.__number_of_bit < 1:
            raise InvalidType("Xnor")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("Xnor")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("Xnor")
        
        
    def __execute(self):
        for i in range(self.__number_of_bit):
            self.__output += "1" if  (not int(self.__input_a[i]) | int(self.__input_b[i])) else "0"
            
    
    def get_output(self) -> str:
        return str(self.__output)
            
        