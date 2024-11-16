from utils import InvalidType, InvalidOperation, ALU_BIT_LENGTH, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH, OPERATION_BIT_LENGTH
from Comparators import MSB
from Reverse32bit import Reverse32bit

class Shifter32Block:
    def __init__(self, input_bits: str, shift_amount: str, operation: str):
        self.__input_bits = input_bits
        self.__shift_amount = shift_amount
        self.__operation = operation
        self.__output = None
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if len(self.__input_bits) != ALU_BIT_LENGTH:
            raise InvalidType("ShifterBlock")
        if len(self.__shift_amount) != SHIFT_AMOUNT_BIT_LENGTH:
            raise InvalidType("ShifterBlock")
        if len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("ShifterBlock")
        for bit in self.__input_bits:
            if bit not in BIT_VALUE:
                raise InvalidType("ShifterBlock")
        for bit in self.__shift_amount:
            if bit not in BIT_VALUE:
                raise InvalidType("ShifterBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("ShifterBlock")
        
    
    def __execute(self):
        pass
        
    
    def get_output(self):
        if self.__output is None:
            raise InvalidOperation("ShifterBlock")
        return str(self.__output)
        