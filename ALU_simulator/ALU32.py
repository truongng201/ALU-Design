from Adders import AddSubBlock
from Comparators import ComparatorBlock
from Gates import Or
from Logical import LogicalBlock
from Shifters import ShifterBlock

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
        if len(self.__input_a) != 32 or len(self.__input_b) != 32 or len(self.__operation) != 4 or len(self.__shift_amount) != 5:
            raise TypeError("ALU32: Invalid input")
        for bit in self.__input_a:
            if bit not in ["0", "1"]:
                raise TypeError("ALU32: Invalid input")
        for bit in self.__input_b:
            if bit not in ["0", "1"]:
                raise TypeError("ALU32: Invalid input")
        for bit in self.__operation:
            if bit not in ["0", "1"]:
                raise TypeError("ALU32: Invalid input")
        for bit in self.__shift_amount:
            if bit not in ["0", "1"]:
                raise TypeError("ALU32: Invalid input")
            
        
    def __execute(self):
        adder = AddSubBlock(self.__input_a, self.__input_b, self.__operation)
        comparator = ComparatorBlock(self.__input_a, self.__input_b, self.__operation)
        logical = LogicalBlock(self.__input_a, self.__input_b, self.__operation)
        shifter = ShifterBlock(self.__input_b, self.__shift_amount, self.__operation)
        
        self.__output = Or(adder.get_output(), comparator.get_output())
        self.__output = Or(self.__output, logical.get_output())
        self.__output = Or(self.__output, shifter.get_output())
        self.__overflow = adder.get_overflow()
        
        
    def get_output(self) -> str:
        if self.__output is None:
            raise ValueError("ALU32: Output is not ready")
        return str(self.__output)
    
    
    def get_overflow(self) -> str:
        if self.__overflow is None:
            raise ValueError("ALU32: Output is not ready")
        return str(self.__overflow)