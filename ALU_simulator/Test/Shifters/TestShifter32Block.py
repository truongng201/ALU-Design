import random

from ALU_simulator.Shifters import Shifter32Block

MIN_INT = -2**31
MAX_INT = 2**31 - 1
MOD = 2**32

class TestShifter32Block:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            Sa = random.randint(0, 31)
            Op = random.choice([0, 1, 12, 13])

            if Op == 0 or Op == 1:
                C = A << Sa
            elif Op == 12:
                if A < 0:
                    A = A + MOD
                C = A >> Sa
            elif Op == 13:
                C = A >> Sa
                
            if C > MAX_INT or C < MIN_INT:
                C = C % MOD
            
            if A < 0:
                A = A + MOD
            if C < 0:
                C = C + MOD
                
            A = bin(A)[2:].zfill(32)
            C = bin(C)[2:].zfill(32)
            Sa = bin(Sa)[2:].zfill(5)
            Op = bin(Op)[2:].zfill(4)
                
            shifter32block = Shifter32Block(A, Sa, Op)
            assert shifter32block.get_output() == C, f"Shifter32Block: Test case {i + 1} failed with A: {A}, Sa={Sa}, Op={Op}. Expected {C} but got {shifter32block.get_output()}"
        print("Shifter32Block: All test cases passed")
    