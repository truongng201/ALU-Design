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
            if bit not in ["0", "1"]:
                raise TypeError("FlipMirror32bit: Invalid input")
        if len(self.__input) != 32:
            raise TypeError("FlipMirror32bit: Invalid input")
    

    def get_output(self) -> str:
        return str(self.__output)