class Not:
    def __init__(self, number_of_bit: int, input_a: str) -> None:
        self.__output = ""
        self.__number_of_bit = number_of_bit
        self.__input_a = input_a
        self.__validate_input()
        self.__execute()
        
        
    def __validate_input(self):
        if self.__number_of_bit != len(self.__input_a):
            raise TypeError("Not: Invalid type")
        if self.__number_of_bit < 1:
            raise TypeError("Not: Invalid type")
        for bit in self.__input_a:
            if bit not in ("0", "1"):
                raise TypeError("Not: Invalid type")
        
    def __execute(self):
        for i in range(self.__number_of_bit):
            self.__output += str(int(not int(self.__input_a[i])))
            
    
    def get_output(self) -> str:
        return self.__output
            
        