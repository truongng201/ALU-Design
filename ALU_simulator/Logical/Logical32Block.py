from utils import InvalidType, InvalidOperation, BIT_VALUE, OPERATION_BIT_LENGTH
from Gates import And, Or, Xor, Xnor
from Plexers import Mux

class Logical32Block:
    def __init__(self, input_a: str, input_b: str, operation: str):
        self.__BIT_LENGTH = 32
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = None
        self.__select_bits = None
        self.__enable_mux = 0
        self.__select_operation()
        self.__validate_input()
        self.__execute()
        
    
    def __select_operation(self):
        first_min_term = int(self.__operation[1]) and (not int(self.__operation[2])) and (not int(self.__operation[3]))
        second_min_term = int(self.__operation[1]) and int(self.__operation[2]) and (not int(self.__operation[3]))
        third_min_term = (not int(self.__operation[1])) and (not int(self.__operation[2])) and int(self.__operation[3])
        fourth_min_term = (not int(self.__operation[1])) and int(self.__operation[2]) and int(self.__operation[3])
        self.__select_bits = first_min_term or second_min_term or third_min_term or fourth_min_term
        
    
    def __validate_input(self):
        if len(self.__input_a) != self.__BIT_LENGTH \
            or len(self.__input_b) != self.__BIT_LENGTH \
            or len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("LogicalBlock")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("LogicalBlock")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("LogicalBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("LogicalBlock")
    
    
    def __execute(self):
        and_result = And(self.__input_a, self.__input_b).get_output()
        or_result = Or(self.__input_a, self.__input_b).get_output()
        xor_result = Xor(self.__input_a, self.__input_b).get_output()
        xnor_result = Xnor(self.__input_a, self.__input_b).get_output()
        self.__output = Mux(
            [and_result, or_result, xor_result, xnor_result],
            str(self.__select_bits),
            enable=str(self.__enable_mux)
        )
    
    
    def get_output(self):
        if self.__output is None:
            raise InvalidOperation("LogicalBlock")
        return str(self.__output)