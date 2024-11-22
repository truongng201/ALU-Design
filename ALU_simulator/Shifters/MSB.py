from ALU_simulator.utils import InvalidType, BIT_VALUE, ALU_BIT_LENGTH

class MSB:
    def __init__(self, input_a: str):
        self.__input_a = input_a
        self.__output = ""
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        self.__output = self.__input_a[0]
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("MSB")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("MSB")
    
    
    def get_output(self) -> str:
        return str(self.__output)