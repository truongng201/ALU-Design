import random

from ALU_simulator.ALU32 import ALU32

MAX_INT = 2**31 - 1
MIN_INT = -2**31
MOD = 2**32

class TestALU32:
    def __init__(self):
        self.__alu = ALU32()
        
        
    def __generate_edge_cases(self):
        pass
    
    
    def __generate_random_cases(self):
        pass
    
    
    def __get_result(self, input_a, input_b, op_code, shift_amount):
        output_c = None
        overflow_v = 0
        # Shift left logical
        if op_code == 0 or op_code == 1:
            output_c = input_b << shift_amount
            if output_c > MAX_INT or output_c < MIN_INT:
                output_c = output_c % MOD
            return output_c, overflow_v
        
        # Add operation
        if op_code == 2 or op_code == 3:
            output_c = input_a + input_b
            if output_c > MAX_INT or output_c < MIN_INT:
                output_c = output_c % MOD
                overflow_v = 1
            return output_c, overflow_v
        
        # And operation
        if op_code == 4:
            output_c = input_a & input_b
            return output_c, overflow_v

        # Or operation
        if op_code == 5:
            output_c = input_a | input_b
            return output_c, overflow_v
        
        # Subtract operation
        if op_code == 6 or op_code == 7:
            output_c = input_a - input_b
            if output_c > MAX_INT or output_c < MIN_INT:
                output_c = output_c % MOD
                overflow_v = 1
            return output_c, overflow_v
        
        # Not equal operation
        if op_code == 8:
            output_c = 1 if input_a != input_b else 0
            return output_c, overflow_v
        
        # Equal operation
        if op_code == 9:
            output_c = 1 if input_a == input_b else 0
            return output_c, overflow_v

        
        # Xor operation
        if op_code == 10:
            output_c = input_a ^ input_b
            return output_c, overflow_v
        
        # Nor operation
        if op_code == 11:
            output_c = ~(input_a | input_b)
            return output_c, overflow_v

        # Shift right logical operation
        if op_code == 12:
            if input_b < 0:
                input_b = input_b + MOD
            output_c = input_b >> shift_amount	
            return output_c, overflow_v
        
        # Shift right arithmetic operation
        if op_code == 13:
            output_c = input_b >> shift_amount
            if output_c > MAX_INT or output_c < MIN_INT:
                output_c = output_c % MOD
            return output_c, overflow_v
        
        # A less than or equal to zero
        if op_code == 14:
            output_c = 1 if input_a <= 0 else 0
            return output_c, overflow_v
        
        # A greater than zero
        if op_code == 15:
            output_c = 1 if input_a > 0 else 0
            return output_c, overflow_v
        
        return None, None