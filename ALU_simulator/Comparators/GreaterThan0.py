from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH
from ALU_simulator.Gates import And, Not
from ALU_simulator.Comparators.IsEqual0 import IsEqual0
from ALU_simulator.Shifters.MSB import MSB

class GreaterThan0:
    def __init__(self, input_a: str):
        self.__input_a = input_a
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        MSB_gate1 = MSB(self.__input_a)
        IsEqual0_gate1 = IsEqual0(self.__input_a)
        Not_gate1 = Not(1, IsEqual0_gate1.get_output())
        Not_gate2 = Not(1, MSB_gate1.get_output())
        And_gate1 = And(1, Not_gate1.get_output(), Not_gate2.get_output())
        self.__output = And_gate1.get_output()
        
    
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("GreaterThan0")
        for i in range(ALU_BIT_LENGTH):
            if self.__input_a[i] not in BIT_VALUE:
                raise InvalidType("GreaterThan0")
    
    
    def get_output(self):
        return str(self.__output)