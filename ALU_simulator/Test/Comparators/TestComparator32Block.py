import random

from ALU_simulator.Comparators.Comparator32Block import Comparator32Block

MIN_INT = -2**31
MAX_INT = 2**31 - 1

class TestComparator32Block:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Op = random.choice([8, 9, 14, 15])
            
            if Op == 8:
                C = 1 if A != B else 0
            elif Op == 9:
                C = 1 if A == B else 0
            elif Op == 14:
                C = 1 if A <= 0 else 0
            elif Op == 15:
                C = 1 if A > 0 else 0
            
            if A < 0:
                A = A + (1<<32)
            if B < 0:
                B = B + (1<<32)
            
                
            A = bin(A)[2:].zfill(32)
            B = bin(B)[2:].zfill(32)
            C = bin(C)[2:].zfill(32)
            Op = bin(Op)[2:].zfill(4)
            comparator = Comparator32Block(A, B, operation=Op)
            result = comparator.get_output()
            assert result == C, f"Comparator32Block: Test case number {i+1} failed with A={A}, B={B}, Op={Op}. Expected {C} but got {result}"