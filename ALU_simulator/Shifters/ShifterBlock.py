class ShifterBlock:
    def __init__(self, input_bits: str, shift_amount: str, operation: str):
        self.__input_bits = input_bits
        self.__shift_amount = shift_amount
        self.__operation = operation
        self.__output = None
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if len(self.__input_bits) != 32 or len(self.__shift_amount) != 5 or len(self.__operation) != 4:
            raise TypeError("ShifterBlock: Invalid input")
        for bit in self.__input_bits:
            if bit not in ["0", "1"]:
                raise TypeError("ShifterBlock: Invalid input")
        for bit in self.__shift_amount:
            if bit not in ["0", "1"]:
                raise TypeError("ShifterBlock: Invalid input")
        for bit in self.__operation:
            if bit not in ["0", "1"]:
                raise TypeError("ShifterBlock: Invalid input")
            
    
    def __execute(self):
        pass
        
    
    def get_output(self):
        if self.__output is None:
            raise ValueError("ShifterBlock: Output is not ready")
        return str(self.__output)
        