from ALU_simulator.utils import InvalidType, ALU_BIT_LENGTH, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH, OPERATION_BIT_LENGTH
from ALU_simulator.Shifters.MSB import MSB
from ALU_simulator.Shifters.Reverse32bit import Reverse32bit

class Shifter32Block:
    def __init__(self, input_bits: str, shift_amount: str, operation: str):
        self.__input_bits = input_bits
        self.__shift_amount = shift_amount
        self.__operation = operation
        self.__output = ""
        self.__select_bits = ""
        self.__enable_mux = ""
        self.__select_operation()
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
        
    
    def __select_operation(self):
        operation3 = int(self.__operation[0])
        operation2 = int(self.__operation[1])
        operation1 = int(self.__operation[2])
        operation0 = int(self.__operation[3])
        
        # not operation3 and not operation2 and not operation1
        first_min_term = (~ operation3) & (~ operation2) & (~ operation1)
        # operation3 and operation2 and not operation1 and not operation0
        second_min_term = operation3 & operation2 & (~ operation1) & (not operation0)
        # operation3 and operation2 and not operation1 and operation0
        third_min_term = operation3 and operation2 and (not operation1) and operation0
        
        self.__enable_mux = "1" if first_min_term or second_min_term or third_min_term else "0"
        self.__select_bits = "1" if second_min_term or third_min_term else "0"
        
    
    def __execute(self):
        pass
        
    
    def get_output(self) -> str:
        return str(self.__output)
        