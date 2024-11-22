from ALU_simulator.utils import InvalidType, BIT_VALUE

class BitExtend1to32:
    def __init__(self, input_a: str) -> None:
        self.__input_a = input_a
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
    
    def __execute(self) -> None:
        self.__output = "0" * 31 + self.__input_a
        
    
    def __validate_input(self) -> None:
        if self.__input_a not in BIT_VALUE:
            raise InvalidType("BitExtend1to32")
        
        
    def get_output(self) -> str:
        return str(self.__output)