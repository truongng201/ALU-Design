from utils import InvalidType, InvalidOperation, BIT_VALUE
from Gates import AND, OR, NOT, XOR


class ComparatorBlock:
    def __init__(self, input_a: str, input_b: str, operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = None
        self.__validate_input()
        self.__execute()


    def __validate_input(self):
        if len(self.__input_a) != 32 or len(self.__input_b) != 32 or len(self.__operation) != 4:
            raise TypeError("ComparatorBlock: Invalid input")
        for bit in self.__input_a:
            if bit not in ["0", "1"]:
                raise TypeError("ComparatorBlock: Invalid input")
        for bit in self.__input_b:
            if bit not in ["0", "1"]:
                raise TypeError("ComparatorBlock: Invalid input")
        for bit in self.__operation:
            if bit not in ["0", "1"]:
                raise TypeError("ComparatorBlock: Invalid input")
    
    
    def __execute(self):
        pass
    
    
    def get_output(self):
        if self.__output is None:
            raise ValueError("ComparatorBlock: Output is not ready")
        return str(self.__output)