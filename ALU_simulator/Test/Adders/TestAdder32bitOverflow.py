import random

from ALU_simulator.Adders import Adder32bitOverflow

MIN_INT = -2**31
MAX_INT = 2**31 - 1
MOD = 2**32

class TestAdder32bitOverflow:
    def __init__(self):
        for _ in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Cin = random.choice([0, 1])    
            C = A + B + Cin
            V = 0
            if C > MAX_INT or C < MIN_INT:
                C = C % MOD
                V = 1
                
            if A < 0:
                A = A + (1<<32)
            if B < 0:
                B = B + (1<<32)
            if C < 0:
                C = C + (1<<32)
                
            A = bin(A)[2:].zfill(32)
            B = bin(B)[2:].zfill(32)
            C = bin(C)[2:].zfill(32)
            

            adder = Adder32bitOverflow(A, B, carry_in=str(Cin))
            result = adder.get_output()
            assert result == C and adder.get_overflow() == str(V), f"Adder32bitOverflow: Test case failed with A={A}, B={B}, Cin={Cin}. Expected {C} but got {result}"
        print("Adder32bitOverflow: All test cases passed")