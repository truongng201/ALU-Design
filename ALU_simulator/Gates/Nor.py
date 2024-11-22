from ALU_simulator.utils import InvalidType, BIT_VALUE

class Nor:
    def __init__(self, number_of_bit: int, input_a: str, input_b: str):
        self.__output = ""
        self.__number_of_bit = number_of_bit
        self.__input_a = input_a
        self.__input_b = input_b
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if len(self.__input_a) != len(self.__input_b):
            raise InvalidType("Nor")
        if self.__number_of_bit != len(self.__input_a):
            raise InvalidType("Nor")
        if self.__number_of_bit < 1:
            raise InvalidType("Nor")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("Nor")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("Nor")
        
        
    def __execute(self):
        for i in range(self.__number_of_bit):
            self.__output += str(int(not (int(self.__input_a[i]) or int(self.__input_b[i]))))
            
    
    def get_output(self) -> str:
        return str(self.__output)
            
        