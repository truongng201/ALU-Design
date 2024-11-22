from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH
from ALU_simulator.Comparators.IsEqual0 import IsEqual0
from ALU_simulator.Shifters.MSB import MSB
from ALU_simulator.Gates import Or

class LessThanOrEqual0:
    def __init__(self, input_a: str):
        self.__input_a = input_a
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        MSB_gate1 = MSB(self.__input_a)
        IsEqual0_gate1 = IsEqual0(self.__input_a)
        Or_gate1 = Or(1, MSB_gate1.get_output(), IsEqual0_gate1.get_output())
        self.__output = Or_gate1.get_output()
        
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("LessThanOrEqual0")
        for i in range(ALU_BIT_LENGTH):
            if self.__input_a[i] not in BIT_VALUE:
                raise InvalidType("LessThanOrEqual0")
    
    
    def get_output(self) -> str:
        return str(self.__output)