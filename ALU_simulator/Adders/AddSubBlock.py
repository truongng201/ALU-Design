from Plexers import Mux
from Adder32bitOverflow import Adder32bitOverflow
from Gates import Xor

class AddSubBlock:
    def __init__(self, input_a: str, input_b: str,  operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = None
        self.__overflow = 0
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if len(self.__input_a) != 32 or len(self.__input_b) != 32 or len(self.__operation) != 4:
            raise TypeError("AddSubBlock: Invalid input")
        for bit in self.__input_a:
            if bit not in ["0", "1"]:
                raise TypeError("AddSubBlock: Invalid input")
        for bit in self.__input_b:
            if bit not in ["0", "1"]:
                raise TypeError("AddSubBlock: Invalid input")
        if self.__carry_in not in ["0", "1"]:
            raise TypeError("AddSubBlock: Invalid input")
        for bit in self.__operation:
            if bit not in ["0", "1"]:
                raise TypeError("AddSubBlock: Invalid input")
        
        
    def __execute(self):
        pass
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("AddSubBlock: Invalid operation")
        return str(self.__output)
    
    