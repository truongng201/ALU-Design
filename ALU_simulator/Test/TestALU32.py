import os
import random

from ALU_simulator.ALU32 import ALU32
from ALU_simulator.utils import InvalidOperation
MAX_INT = 2**31 - 1
MIN_INT = - 2**31
MOD = 2**32
TOTAL_OP_CODE = 16
TOTAL_SHIFT_AMOUNT = 32
SHIFT_OPCODE = [0, 1, 12, 13]
TOTAL_RANDOM_TEST_CASES = 10000
TOTAL_EDGE_TEST_CASES = 4608

class TestALU32:
    def __init__(self):
        self.__total_pass = 0
        self.__fail_test_cases = []
        print("TestALU32: Start testing")
        self.__generate_edge_cases()
        self.__generate_random_cases()
        print("-"*10)
        for test_case in self.__fail_test_cases:
            print(test_case)
        print("TestALU32: Total pass: ", self.__total_pass)
        print("TestALU32: Total fail: ", TOTAL_RANDOM_TEST_CASES + TOTAL_EDGE_TEST_CASES - self.__total_pass)
        print("TestALU32: Finish testing")
        
        
    def __generate_edge_cases(self):
        edge_cases = [(MAX_INT, MIN_INT), (MIN_INT, MAX_INT), (MAX_INT, MAX_INT), (MIN_INT, MIN_INT), (0, 0), (0, MAX_INT), (0, MIN_INT), (MAX_INT, 0), (MIN_INT, 0)]
        for edge_case in edge_cases:
            for Op in range(TOTAL_OP_CODE):
                A = edge_case[0]
                B = edge_case[1]
                for Sa in range(TOTAL_SHIFT_AMOUNT):
                    C, V = self.__get_result(A, B, Op, Sa)
                    if C == None or V == None:
                        raise InvalidOperation("TestALU32")
                
                    self.__run_test(A, B, C, V, Op, Sa)  
    
    
    
    def __generate_random_cases(self):
        for _ in range(TOTAL_RANDOM_TEST_CASES):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Op = random.randint(0, TOTAL_OP_CODE - 1)
            Sa = random.randint(0, TOTAL_SHIFT_AMOUNT - 1)
            
            C, V = self.__get_result(A, B, Op, Sa)
            
            
            self.__run_test(A, B, C, V, Op, Sa)            
    
    
    def __run_test(self, A, B, C, V, Op, Sa):
        if A < 0:
            A = A + MOD
        if B < 0:
            B = B + MOD
        if C < 0:
            C = C + MOD
        
        A = bin(A)[2:].zfill(32)
        B = bin(B)[2:].zfill(32)
        C = bin(C)[2:].zfill(32)
        V = str(V)
        Op = bin(Op)[2:].zfill(4)
        Sa = bin(Sa)[2:].zfill(5)
        
        alu = ALU32(A, B, Op, Sa)
        alu_output = alu.get_output()
        alu_overflow = alu.get_overflow()
        if alu_output != C or alu_overflow != V:
            self.__fail_test_cases.append(f"{'-' * 10}\nTestALU32 fail with:\nA = {A}\nB = {B}\nOp = {Op}\nSa = {Sa}\nExpected: {C}, {V}\nGot: {alu_output}, {alu_overflow}")
        else:
            print("-" * 10)
            print(f"A = {A}\nB = {B}\nOp = {Op}\nSa = {Sa}\nOutput = {alu_output}\nOverflow = {alu_overflow}")
            self.__total_pass += 1
    
    
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