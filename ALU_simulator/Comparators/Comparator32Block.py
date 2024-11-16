from utils import InvalidType, InvalidOperation, BIT_VALUE, ALU_BIT_LENGTH, OPERATION_BIT_LENGTH


class Comparator32Block:
    def __init__(self, input_a: str, input_b: str, operation: str):
        self.__input_a = input_a
        self.__input_b = input_b
        self.__operation = operation
        self.__output = None
        self.__validate_input()
        self.__execute()


    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        if len(self.__input_b) != ALU_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        if len(self.__operation) != OPERATION_BIT_LENGTH:
            raise InvalidType("ComparatorBlock")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
        for bit in self.__input_b:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
        for bit in self.__operation:
            if bit not in BIT_VALUE:
                raise InvalidType("ComparatorBlock")
    
    def __execute(self):
        pass
    
    
    def get_output(self):
        if self.__output is None:
            raise InvalidOperation("ComparatorBlock")
        return str(self.__output)