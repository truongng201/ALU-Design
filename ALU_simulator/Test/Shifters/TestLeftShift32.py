import random

from ALU_simulator.Shifters.LeftShift32 import LeftShift32

MIN_INT = -2**31
MAX_INT = 2**31 - 1
MOD = 2**32

class TestLeftShift32:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            Cin = random.randint(0, 1)
            Sa = random.randint(0, 31)
            C = A * (2 ** Sa) + Cin * (2 ** Sa - 1)
            
            if C > MAX_INT or C < MIN_INT:
                C = C % MOD
            
            if A < 0:
                A = A + MOD
            if C < 0:
                C = C + MOD
                
            A = bin(A)[2:].zfill(32)
            C = bin(C)[2:].zfill(32)
            Sa = bin(Sa)[2:].zfill(5)
            
            leftshifter = LeftShift32(A, str(Cin), Sa)
            result = leftshifter.get_output()
            assert result == C, f"LeftShift32: Test case number {i+1} failed with A={A}, Cin={Cin}, Sa={Sa}. Expected {C} but got {result}"
        print(f"LeftShift32: All test cases passed")