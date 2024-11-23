from ALU_simulator.Plexers import Mux
from ALU_simulator.Adders.Adder32bitOverflow import Adder32bitOverflow
from ALU_simulator.Gates import Not
from ALU_simulator.utils import InvalidType, BIT_VALUE, OPERATION_BIT_LENGTH, ALU_BIT_LENGTH

class AddSub32Block:
    def __init__(self, input_a: str, input_b: str,  operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = ""
        self.__carry_in = ""
        self.__enable_mux = ""
        self.__overflow = 0
        self.__select_bits = ""
        self.__select_operation()
        self.__validate_input()
        self.__execute()
        
    
    def __select_operation(self):
        operation3 = int(self.__operation[0])
        operation2 = int(self.__operation[1])
        operation1 = int(self.__operation[2])
        
        # not operation3 and not operation2 and operation1
        first_min_term = (~ operation3) & (~ operation2) & operation1
        # not operation3 and operation2 and operation1
        second_min_term = (~ operation3) & operation2 & operation1
        
        self.__enable_mux = str(first_min_term | second_min_term)
        self.__carry_in = str(second_min_term)
        self.__select_bits = str(second_min_term)
    
        
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH \
            or len(self.__input_b) != ALU_BIT_LENGTH \
            or len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("AddSubBlock")
        for i in range(ALU_BIT_LENGTH):
            if self.__input_a[i] not in BIT_VALUE or self.__input_b[i] not in BIT_VALUE:
                raise InvalidType("AddSubBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("AddSubBlock")
        
        
    def __execute(self):
        self.__input_b = Mux(
            [self.__input_b, Not(ALU_BIT_LENGTH, self.__input_b).get_output()], 
            select_bit=self.__select_bits, 
            enable=self.__enable_mux
        ).get_output()
        
        adder = Adder32bitOverflow(self.__input_a, self.__input_b, self.__carry_in)
        self.__output = adder.get_output()
        self.__overflow = adder.get_overflow()
        
        self.__output = Mux(
            ["", self.__output], 
            select_bit=self.__enable_mux, 
            enable=self.__enable_mux
        ).get_output()
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def get_output(self) -> str:
        return str(self.__output)
    
    