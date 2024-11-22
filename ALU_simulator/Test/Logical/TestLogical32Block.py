import random

from ALU_simulator.Logical import Logical32Block

MIN_INT = -2**31
MAX_INT = 2**31 - 1

class TestLogical32Block:
    def __init__(self):
        for i in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Op = random.choice([4, 5, 10, 11])
            C = None
            if Op == 4:
                C = A & B
            elif Op == 5:
                C = A | B
            elif Op == 10:
                C = A ^ B
            elif Op == 11:
                C = ~ (A | B)
            
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
            
            logical = Logical32Block(A, B, operation=Op)
            result = logical.get_output()
            assert result == C, f"Logical32Block: Test case number {i + 1} failed with A={A}, B={B}, Op={Op}. Expected {C} but got {result}"
        print("Logical32Block: All test cases passed")