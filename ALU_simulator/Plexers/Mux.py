from ALU_simulator.utils import InvalidInput, BIT_VALUE, OPERATION_BIT_LENGTH

class Mux:
    def __init__(self, inputs: list[str], select_bit: str, enable = 1) -> None:
        self.__inputs = inputs
        self.__select_bit = select_bit
        self.__data_width = 0
        self.__output = None
        self.__enable = enable
        self.__validate_input()
        self.__execute()
        
    
    def __execute(self):
        for data in self.__inputs:
            if data != None:
                self.__data_width = len(data)
                break
        if self.__enable == 0:
            self.__output = "0" * self.__data_width
            return
        select_data = int(self.__select_bit, 2)
        if select_data >= len(self.__inputs) or self.__inputs[select_data] == None:
            self.__output = "0" * self.__data_width
        else:
            self.__output = self.__inputs[select_data]
        
        
    def __validate_input(self):
        for bit in self.__select_bit:
            if bit not in BIT_VALUE:
                raise InvalidInput("Mux")
        if len(self.__select_bit) <= 0 or len(self.__select_bit) >= OPERATION_BIT_LENGTH:
            raise InvalidInput("Mux")
        if len(self.__inputs) > 2 ** len(self.__select_bit):
            raise InvalidInput("Mux")
        if str(self.__enable) not in BIT_VALUE:
            raise InvalidInput("Mux")
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("Mux: Invalid operation")
        return str(self.__output)