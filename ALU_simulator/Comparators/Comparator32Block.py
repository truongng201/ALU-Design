from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH, OPERATION_BIT_LENGTH
from ALU_simulator.Comparators.BitExtend1to32 import BitExtend1to32
from ALU_simulator.Comparators.IsEqual import IsEqual
from ALU_simulator.Comparators.LessThanOrEqual0 import LessThanOrEqual0
from ALU_simulator.Comparators.GreaterThan0 import GreaterThan0
from ALU_simulator.Plexers import Mux
from ALU_simulator.Gates import Not

class Comparator32Block:
    def __init__(self, input_a: str, input_b: str, operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = ""
        self.__enable_mux = ""
        self.__select_bits = ""
        self.__select_operation()
        self.__validate_input()
        self.__execute()
        
        
    def __select_operation(self):
        operation3 = int(self.__operation[0]) == 1
        operation2 = int(self.__operation[1]) == 1
        operation1 = int(self.__operation[2]) == 1
        operation0 = int(self.__operation[3]) == 1
        
        # operation3 and not operation2 and not operation1 and not operation0
        first_min_term = operation3 and (not operation2) and (not operation1) and (not operation0)
        # operation3 and not operation2 and not operation1 and operation0
        second_min_term = operation3 and (not operation2) and (not operation1) and operation0
        # operation3 and operation2 and operation1 and not operation0
        third_min_term = operation3 and operation2 and operation1 and (not operation0)
        # operation3 and operation2 and operation1 and operation0
        fourth_min_term = operation3 and operation2 and operation1 and operation0
        
        self.__enable_mux = str(int(first_min_term or second_min_term or third_min_term or fourth_min_term))
        self.__select_bits = str(int(second_min_term | fourth_min_term)) + str(int(third_min_term | fourth_min_term))


    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        if len(self.__input_b) != ALU_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        if len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
    
    def __execute(self):
        equal = IsEqual(self.__input_a, self.__input_b).get_output()
        less_than_or_equal_0 = LessThanOrEqual0(self.__input_a).get_output()
        greater_than_0 = GreaterThan0(self.__input_a).get_output()
        
        notequal = BitExtend1to32(Not(1, equal).get_output()).get_output()
        equal = BitExtend1to32(equal).get_output()
        less_than_or_equal_0 = BitExtend1to32(less_than_or_equal_0).get_output()
        greater_than_0 = BitExtend1to32(greater_than_0).get_output()
        self.__output = Mux(
            [notequal, equal, less_than_or_equal_0, greater_than_0],
            select_bit=self.__select_bits,
            enable=self.__enable_mux
        ).get_output()
    
    
    def get_output(self) -> str:
        return str(self.__output)