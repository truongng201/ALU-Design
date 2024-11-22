from ALU_simulator.utils import InvalidType, BIT_VALUE

class Not:
    def __init__(self, number_of_bit: int, input_a: str):
        self.__output = ""
        self.__number_of_bit = number_of_bit
        self.__input_a = input_a
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if self.__number_of_bit != len(self.__input_a):
            raise InvalidType("Not")
        if self.__number_of_bit < 1:
            raise InvalidType("Not")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("Not")
        
    def __execute(self):
        for i in range(self.__number_of_bit):
            self.__output += str(int(not int(self.__input_a[i])))
            
    
    def get_output(self) -> str:
        return str(self.__output)
            
        