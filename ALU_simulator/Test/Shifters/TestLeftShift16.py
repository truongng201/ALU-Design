import random

from ALU_simulator.Shifters.LeftShift16 import LeftShift16

MIN_INT = -2**31
MAX_INT = 2**31 - 1
MOD = 2**32

class TestLeftShift16:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            Cin = random.randint(0, 1)
            C = A * (2 ** 16) + Cin * (2 ** 16 - 1)
            
            if C > MAX_INT or C < MIN_INT:
                C = C % MOD
            
            if A < 0:
                A = A + (1<<32)
            if C < 0:
                C = C + (1<<32)
                
            A = bin(A)[2:].zfill(32)
            C = bin(C)[2:].zfill(32)
            
            leftshifter = LeftShift16(A, str(Cin))
            result = leftshifter.get_output()
            assert result == C, f"LeftShift16: Test case number {i+1} failed with A={A}, Cin={Cin}. Expected {C} but got {result}"
        print(f"LeftShift16: All test cases passed")