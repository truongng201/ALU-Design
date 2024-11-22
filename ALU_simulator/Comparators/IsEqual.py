from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH
from ALU_simulator.Gates import Xor
from ALU_simulator.Comparators.IsEqual0 import IsEqual0

class IsEqual:
    def __init__(self, input_a: str, input_b: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
    
    def __execute(self):
        Xor_gate1 = Xor(32, self.__input_a, self.__input_b)
        self.__output = Xor_gate1.get_output()
        self.__output = IsEqual0(self.__output).get_output()    
    
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH and len(self.__input_b) != ALU_BIT_LENGTH:
            raise InvalidType("IsEqual")
        for i in range(ALU_BIT_LENGTH):
            if self.__input_a[i] not in BIT_VALUE or self.__input_b[i] not in BIT_VALUE:
                raise InvalidType("IsEqual")
            
    
    def get_output(self) -> str:
        return str(self.__output)