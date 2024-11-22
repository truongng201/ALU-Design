from ALU_simulator.utils import InvalidType, BIT_VALUE, OPERATION_BIT_LENGTH, ALU_BIT_LENGTH
from ALU_simulator.Gates import And, Or, Xor, Xnor
from ALU_simulator.Plexers import Mux

class Logical32Block:
    def __init__(self, input_a: str, input_b: str, operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = ""
        self.__select_bits = ""
        self.__enable_mux = ""
        self.__select_operation()
        self.__validate_input()
        self.__execute()
        
    
    def __select_operation(self):
        operation3 = True if int(self.__operation[0]) == 1 else False
        operation2 = True if int(self.__operation[1]) == 1 else False
        operation1 = True if int(self.__operation[2]) == 1 else False
        operation0 = True if int(self.__operation[3]) == 1 else False
        
        # not operation3 and operation2 and not operation1 and operation0
        first_min_term = (not operation3) and operation2 and (not operation1) and operation0
        # operation3 and not operation2 and operation1 and operation0
        second_min_term = operation3 and (not operation2) and operation1 and operation0
        # operation3 and not operation2 and operation1 and not operation0
        third_min_term = operation3 and (not operation2) and operation1 and (not operation0)
        # not operation3 and operation2 and not operation1 and not operation0
        fourth_min_term = (not operation3) and operation2 and (not operation1) and (not operation0)

        self.__enable_mux = "1" if first_min_term or second_min_term or third_min_term or fourth_min_term else "0"
        first_or = "1" if first_min_term or second_min_term else "0"
        second_or = "1" if second_min_term or third_min_term else "0"
        self.__select_bits = second_or + first_or
    
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH \
            or len(self.__input_b) != ALU_BIT_LENGTH \
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
        and_result = And(ALU_BIT_LENGTH, self.__input_a, self.__input_b).get_output()
        or_result = Or(ALU_BIT_LENGTH, self.__input_a, self.__input_b).get_output()
        xor_result = Xor(ALU_BIT_LENGTH, self.__input_a, self.__input_b).get_output()
        xnor_result = Xnor(ALU_BIT_LENGTH, self.__input_a, self.__input_b).get_output()
        self.__output = Mux(
            [and_result, or_result, xor_result, xnor_result],
            select_bit=self.__select_bits,
            enable=self.__enable_mux
        ).get_output()
    
    
    def get_output(self) -> str:
        return str(self.__output)