import random

from ALU_simulator.Adders import Adder16bitOverflow

MIN_INT = -2**15
MAX_INT = 2**15 - 1

class TestAdder16bitOverflow:
    def __init__(self):
        for _ in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Cin = random.choice([0, 1])   
            V = 0 
            C = A + B + Cin
            
            if C > MAX_INT or C < MIN_INT:
                C = C % (2**16)
                V = 1
            if A < 0:
                A = A + (1<<16)
            if B < 0:
                B = B + (1<<16)
            if C < 0:
                C = C + (1<<16)
            A = bin(A)[2:].zfill(16)
            B = bin(B)[2:].zfill(16)
            C = bin(C)[2:].zfill(16)

            adder = Adder16bitOverflow(A, B, carry_in=str(Cin))
            result = adder.get_output()
            assert result == C and adder.get_overflow() == str(V), f"Adder16bitOverlow: Test case failed with A={A}, B={B}, Cin={Cin}. Expected {C} but got {result}"
        print("Adder16bitOverflow: All test cases passed")