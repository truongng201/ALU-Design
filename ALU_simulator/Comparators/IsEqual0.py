from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH, OPERATION_BIT_LENGTH
from ALU_simulator.Gates import Or, Not

class IsEqual0:
    def __init__(self, input_a: str) -> None:
        self.__input_a = input_a
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
    
    def __execute(self) -> None:
        or_gate1 = Or(8, self.__input_a[:8], self.__input_a[8:16])
        or_gate2 = Or(8, or_gate1.get_output(), self.__input_a[16:24])
        or_gate3 = Or(8, or_gate2.get_output(), self.__input_a[24:32])
        
        self.__output = or_gate3.get_output()
        
        or_gate1 = Or(2, self.__output[:2], self.__output[2:4])
        or_gate2 = Or(2, or_gate1.get_output(), self.__output[4:6])
        or_gate3 = Or(2, or_gate2.get_output(), self.__output[6:8])
        
        self.__output = or_gate3.get_output()
        
        or_gate1 = Or(1, self.__output[:1], self.__output[1:2])
        self.__output = Not(1, or_gate1.get_output()).get_output()
        
        
    def __validate_input(self) -> None:
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("IsEqual0")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("IsEqual0")
            
    
    def get_output(self) -> str:
        return str(self.__output)   