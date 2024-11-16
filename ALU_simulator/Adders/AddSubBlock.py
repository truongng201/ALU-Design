from Plexers import Mux
from Adder32bitOverflow import Adder32bitOverflow
from Gates import Not
from utils import InvalidType, InvalidOperation, BIT_VALUE, OPERATION_BIT_LENGTH

class AddSubBlock:
    def __init__(self, input_a: str, input_b: str,  operation: str):
        self.__BIT_LENGTH = 32
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = None
        self.__carry_in = None
        self.__enable_mux = None
        self.__overflow = 0
        self.__select_bits = None
        self.__select_operation()
        self.__validate_input()
        self.__execute()
        
    
    def __select_operation(self):
        first_min_term = int(self.__operation[1]) and (not int(self.__operation[2])) and (not int(self.__operation[3]))
        second_min_term = int(self.__operation[1]) and int(self.__operation[2]) and (not int(self.__operation[3]))
        self.__enable_mux = first_min_term or second_min_term
        self.__carry_in = str(second_min_term)
        self.__select_bits = second_min_term
    
        
    def __validate_input(self):
        if len(self.__input_a) != self.__BIT_LENGTH \
            or len(self.__input_b) != self.__BIT_LENGTH \
            or len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("AddSubBlock")
        for i in range(self.__BIT_LENGTH):
            if self.__input_a[i] not in BIT_VALUE or self.__input_b[i] not in BIT_VALUE:
                raise InvalidType("AddSubBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("AddSubBlock")
        
        
    def __execute(self):
        self.__input_b = Mux(
            [self.__input_b, Not(self.__BIT_LENGTH, self.__input_b)], 
            str(self.__select_bits), 
            enable=self.__enable_mux
        ).get_output()
        
        adder = Adder32bitOverflow(self.__input_a, self.__input_b, self.__carry_in)
        self.__output = adder.get_output()
        self.__overflow = adder.get_overflow()
        
        self.__output = Mux(
            [None, self.__output], 
            str(self.__select_bits), 
            enable=self.__enable_mux
        ).get_output()
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def get_output(self) -> str:
        if self.__output == None:
            raise InvalidOperation("AddSubBlock")
        return str(self.__output)
    
    