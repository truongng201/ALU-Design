import random

from ALU_simulator.Adders import Adder4bitOverflow

MIN_INT = 0
MAX_INT = 2**3 - 1

class TestAdder4bitOverflow:
    def __init__(self):
        for _ in range(1000):
            A = random.randint(MIN_INT, MAX_INT)
            B = random.randint(MIN_INT, MAX_INT)
            Cin = random.choice(["0", "1"])    
            C = A + B
            if Cin == "1":
                C += 1
            A = bin(A)[2:].zfill(4)
            B = bin(B)[2:].zfill(4)
            C = bin(C)[2:].zfill(4)

            adder = Adder4bitOverflow(A, B, carry_in=Cin)
            result = adder.get_output()
            assert result == C, f"Adder4bit: Test case failed with A={A}, B={B}, Cin={Cin}. Expected {C} but got {result}"
        print("Adder4bit: All test cases passed")