from LeftShift1 import LeftShift1

class LeftShift2:
    def __init__(self, input: str, carry_in: int):
        self.__output = None
        self.__input = input
        self.__carry_in = carry_in
        self.__validate_input()
        self.__execute()        


    def __execute(self):
        self.__output = LeftShift1(self.__input, self.__carry_in).get_output()
        self.__output = LeftShift1(self.__output, self.__carry_in).get_output()
    
    
    def __validate_input(self):
        for bit in self.__input:
            if bit not in ["0", "1"]:
                raise TypeError("LeftShift2: Invalid input")
        if len(self.__input) != 32:
            raise TypeError("LeftShift2: Invalid input")
        if self.__carry_in not in [0, 1]:
            raise TypeError("LeftShift2: Invalid input")
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("LeftShift2: Invalid operation")
        return str(self.__output)