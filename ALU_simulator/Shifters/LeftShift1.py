from ALU_simulator.utils import InvalidType,  ALU_BIT_LENGTH, BIT_VALUE

class LeftShift1:
    def __init__(self, input_b: str, carry_in: str):
        self.__output = ""
        self.__input_b = input_b
        self.__carry_in = carry_in
        self.__validate_input()
        self.__execute()
    
    
    def __validate_input(self):
        if len(self.__input_b) != ALU_BIT_LENGTH:
            raise InvalidType("LeftShift1")
        if len(self.__carry_in) != 1:
            raise InvalidType("LeftShift1")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift1")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("LeftShift1")
        
        
    def __execute(self):
        self.__output = self.__input_b[1:] + self.__carry_in
        
    
    def get_output(self) -> str:
        return str(self.__output)
        