from ALU_simulator.utils import InvalidType, ALU_BIT_LENGTH, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH, OPERATION_BIT_LENGTH
from ALU_simulator.Shifters.MSB import MSB
from ALU_simulator.Shifters.Reverse32bit import Reverse32bit
from ALU_simulator.Shifters.LeftShift32 import LeftShift32
from ALU_simulator.Plexers import Mux

class Shifter32Block:
    def __init__(self, input_bits: str, shift_amount: str, operation: str):
        self.__input_bits = input_bits
        self.__shift_amount = shift_amount
        self.__operation = operation
        self.__output = ""
        self.__select_bits = ""
        self.__enable_mux = ""
        self.__carry_in = ""
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
        operation3 = int(self.__operation[0]) == 1
        operation2 = int(self.__operation[1]) == 1
        operation1 = int(self.__operation[2]) == 1
        operation0 = int(self.__operation[3]) == 1
        
        # not operation3 and not operation2 and not operation1
        first_min_term = (not operation3) & (not operation2) & (not operation1)
        # operation3 and operation2 and not operation1 and not operation0
        second_min_term = operation3 and operation2 and (not operation1) and (not operation0)
        # operation3 and operation2 and not operation1 and operation0
        third_min_term = operation3 and operation2 and (not operation1) and operation0
        
        self.__carry_in = str(int(third_min_term))
        self.__enable_mux = str(int(first_min_term or second_min_term or third_min_term))
        self.__select_bits = str(int(third_min_term)) + str(int(second_min_term))
        
    
    def __execute(self):
        reverse_output = Reverse32bit(self.__input_bits).get_output()
        msb_output = MSB(self.__input_bits).get_output()
        
        self.__output = Mux(
            [self.__input_bits, reverse_output, reverse_output, None],
            select_bit=self.__select_bits,
            enable=self.__enable_mux
        ).get_output()
        
        Cin = str(int(int(msb_output) and int(self.__carry_in)))
        self.__output = LeftShift32(self.__output, Cin, self.__shift_amount).get_output()
        reverse_output = Reverse32bit(self.__output).get_output()
        self.__output = Mux(
            [self.__output, reverse_output, reverse_output, None],
            select_bit=self.__select_bits,
            enable=self.__enable_mux
        ).get_output()
    
    def get_output(self) -> str:
        return str(self.__output)
        