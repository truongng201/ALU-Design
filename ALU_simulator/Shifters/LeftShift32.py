from LeftShift1 import LeftShift1
from LeftShift2 import LeftShift2
from LeftShift4 import LeftShift4
from LeftShift8 import LeftShift8
from LeftShift16 import LeftShift16
from Plexers import Mux
from ALU_simulator.utils import InvalidType,  ALU_BIT_LENGTH, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH


class LeftShift32:
    def __init__(self, input: str, carry_in: str, shift_amount: str):
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
        if len(self.__input) != ALU_BIT_LENGTH:
            raise InvalidType("LeftShift32")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("LeftShift32")
        if len(self.__shift_amount) != SHIFT_AMOUNT_BIT_LENGTH:
            raise InvalidType("LeftShift32")
        for bit in self.__input:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift32")
        for bit in self.__shift_amount:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift32")
    
    
    def get_output(self) -> str:
        if self.__output == None:
            raise InvalidOperation("LeftShift32")
        return str(self.__output)