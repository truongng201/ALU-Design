from ALU_simulator.utils import InvalidType, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH, OPERATION_BIT_LENGTH, ALU_BIT_LENGTH
from Adders import AddSub32Block
from Comparators import Comparator32Block
from Gates import Or
from Logical import Logical32Block
from Shifters import Shifter32Block

class ALU32:
    def __init__(self, input_a: str, input_b: str, operation: str, shift_amount: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__shift_amount = shift_amount
        self.__output = None
        self.__overflow = None
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH \
            or len(self.__input_b) != ALU_BIT_LENGTH \
            or len(self.__operation) != OPERATION_BIT_LENGTH \
            or len(self.__shift_amount) != SHIFT_AMOUNT_BIT_LENGTH:
            raise InvalidType("ALU32")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("ALU32")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("ALU32")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("ALU32")
        for bit in self.__shift_amount:
            if bit not in BIT_VALUE:
                raise InvalidType("ALU32")
            
        
    def __execute(self):
        adder = AddSub32Block(self.__input_a, self.__input_b, self.__operation)
        comparator = Comparator32Block(self.__input_a, self.__input_b, self.__operation)
        logical = Logical32Block(self.__input_a, self.__input_b, self.__operation)
        shifter = Shifter32Block(self.__input_b, self.__shift_amount, self.__operation)
        
        self.__output = Or(ALU_BIT_LENGTH, adder.get_output(), comparator.get_output())
        self.__output = Or(ALU_BIT_LENGTH, self.__output, logical.get_output())
        self.__output = Or(ALU_BIT_LENGTH, self.__output, shifter.get_output())
        self.__overflow = adder.get_overflow()
        
        
    def get_output(self) -> str:
        if self.__output is None:
            raise ValueError("ALU32: Output is not ready")
        return str(self.__output)
    
    
    def get_overflow(self) -> str:
        if self.__overflow is None:
            raise ValueError("ALU32: Output is not ready")
        return str(self.__overflow)