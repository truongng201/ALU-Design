from ALU_simulator.Shifters.LeftShift1 import LeftShift1
from ALU_simulator.utils import InvalidType,  ALU_BIT_LENGTH, BIT_VALUE

class LeftShift2:
    def __init__(self, input: str, carry_in: str):
        self.__output = ""
        self.__input = input
        self.__carry_in = carry_in
        self.__validate_input()
        self.__execute()        


    def __execute(self):
        self.__output = LeftShift1(self.__input, self.__carry_in).get_output()
        self.__output = LeftShift1(self.__output, self.__carry_in).get_output()
    
    
    def __validate_input(self):
        if len(self.__input) != ALU_BIT_LENGTH:
            raise InvalidType("LeftShift2")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("LeftShift2")
        for bit in self.__input:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift2")
        
    
    def get_output(self) -> str:
        return str(self.__output)