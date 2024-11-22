from ALU_simulator.utils import BIT_VALUE, InvalidType, ALU_BIT_LENGTH

class Reverse32bit:
    def __init__(self, input: str):
        self.__input = input
        self.__output = None
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        self.__output = self.__input[::-1]
        
    
    def __validate_input(self):
        for bit in self.__input:
            if bit not in BIT_VALUE:
                raise InvalidType("Reverse32bit")
        if len(self.__input) != ALU_BIT_LENGTH:
            raise InvalidType("Reverse32bit")

    def get_output(self) -> str:
        return str(self.__output)