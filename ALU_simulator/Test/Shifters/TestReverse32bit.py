import random

from ALU_simulator.Shifters import Reverse32bit

class TestReverse32bit:
    def __init__(self):
        for i in range(1000):
            input_a = self.__generate_random_input()
            reverse32bit = Reverse32bit(input_a)
            assert reverse32bit.get_output() == input_a[::-1], f"Reverse32bit: Test case {i + 1} failed with input_a: {input_a}"
        print("Reverse32bit: All test cases passed")
        
        
    def __generate_random_input(self) -> str:
        return "".join([random.choice(["0", "1"]) for _ in range(32)])