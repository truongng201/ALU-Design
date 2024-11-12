class LeftShift1:
    def __init__(self, input_b: str, carry_in: int):
        self.__output = None
        self.__input_b = input_b
        self.__carry_in = carry_in
        self.__validate_input()
        self.__execute()


    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("LeftShift1: Invalid operation")
        return str(self.__output)
    
    
    def __validate_input(self):
        if len(self.__input_b) != 32:
            raise TypeError("LeftShift1: Invalid input")
        for bit in self.__input_b:
            if bit not in ["0", "1"]:
                raise TypeError("LeftShift1: Invalid input")
        if self.__carry_in not in [0, 1]:
            raise TypeError("LeftShift1: Invalid input")
        
        
    def __execute(self):
        self.__output = str(self.__carry_in) + self.__input_b[:31]
        