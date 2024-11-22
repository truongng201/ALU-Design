import random

from ALU_simulator.Adders import AddSub32Block

MIN_INT = -2**31
MAX_INT = 2**31 - 1
MOD = 2**32

class TestAddSub32Block:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Op = random.choice([2, 3, 6, 7])
            if Op == 2 or Op == 3:
                C = A + B
                V = 0
                if C > MAX_INT or C < MIN_INT:
                    C = C % MOD
                    V = 1
            elif Op == 6 or Op == 7:
                C = A - B
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
            Op = bin(Op)[2:].zfill(4)
            
            adder = AddSub32Block(A, B, operation=Op)
            result = adder.get_output()
            assert result == C and adder.get_overflow() == str(V), f"AddSub32Block: Test case number {i+1} failed with A={A}, B={B}, Op={Op}. Expected {C} but got {result}"
        print("AddSub32Block: All test cases passed")