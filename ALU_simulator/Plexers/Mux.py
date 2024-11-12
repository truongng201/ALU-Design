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
        self.__data_width = len(self.__inputs[0])
        if self.__enable == 0:
            self.__output = "0" * self.__data_width
            return
        select_data = int(self.__select_bit, 2)
        if select_data >= len(self.__inputs):
            self.__output = "0" * self.__data_width
        else:
            self.__output = self.__inputs[select_data]
        
        
    def __validate_input(self):
        for bit in self.__select_bit:
            if bit not in ["0", "1"]:
                raise TypeError("Mux: Invalid input")
        if len(self.__select_bit) <= 0 or len(self.__select_bit) > 3:
            raise TypeError("Mux: Invalid input")
        if len(self.__inputs) > 2 ** len(self.__select_bit):
            raise TypeError("Mux: Invalid input")
        for input in self.__inputs:
            if len(input) != len(self.__inputs[0]):
                raise TypeError("Mux: Invalid input")
            for bit in input:
                if bit not in ["0", "1"]:
                    raise TypeError("Mux: Invalid input")
        if self.__enable not in [0, 1]:
            raise TypeError("Mux: Invalid input")
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("Mux: Invalid operation")
        return str(self.__output)