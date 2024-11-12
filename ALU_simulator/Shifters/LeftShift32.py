from LeftShift1 import LeftShift1
from LeftShift2 import LeftShift2
from LeftShift4 import LeftShift4
from LeftShift8 import LeftShift8
from LeftShift16 import LeftShift16
from Plexers import Mux


class LeftShift32:
    def __init__(self, input: str, carry_in: int, shift_amount: str):
        self.__output = None
        self.__input = input
        self.__carry_in = carry_in
        self.__shift_amount = shift_amount
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        shift1_output = LeftShift1(self.__input, self.__carry_in).get_output()
        self.__output = Mux([self.__input, shift1_output], self.__shift_amount[0]).get_output()
        shift2_output = LeftShift2(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift2_output], self.__shift_amount[1]).get_output()
        shift4_output = LeftShift4(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift4_output], self.__shift_amount[2]).get_output()
        shift8_output = LeftShift8(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift8_output], self.__shift_amount[3]).get_output()
        shift16_output = LeftShift16(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift16_output], self.__shift_amount[4]).get_output()
    
    
    def __validate_input(self):
        for bit in self.__input:
            if bit not in ["0", "1"]:
                raise TypeError("LeftShift32: Invalid input")
        if len(self.__input) != 32:
            raise TypeError("LeftShift32: Invalid input")
        if self.__carry_in not in [0, 1]:
            raise TypeError("LeftShift32: Invalid input")
        for bit in self.__shift_amount:
            if bit not in ["0", "1"]:
                raise TypeError("LeftShift32: Invalid input")
        if len(self.__shift_amount) != 5:
            raise TypeError("LeftShift32: Invalid input")
    
    
    def get_output(self) -> str:
        if self.__output == None:
            raise ValueError("LeftShift32: Invalid operation")
        return str(self.__output)