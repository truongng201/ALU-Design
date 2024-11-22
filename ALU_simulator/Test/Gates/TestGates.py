import random

from ALU_simulator.Gates import *

MIN_INT = -2**31
MAX_INT = 2**31 - 1

class TestGates:
    def __init__(self):
        for i in range(1000):
            self.__index = i
            self.__input_a = random.randint(MIN_INT, MAX_INT)
            self.__input_b = random.randint(MIN_INT, MAX_INT)
            
            self.__test_and()
            self.__test_or()
            self.__test_nor()
            self.__test_xor()
            self.__test_not()
            self.__test_xnor()
        print("Gates: All test cases pass")
        
    def __test_and(self):
        C = self.__input_a & self.__input_b
        input_a = self.__input_a
        input_b = self.__input_b
        if input_a < 0:
            input_a = input_a + (1<<32)
        if input_b < 0:
            input_b = input_b + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        input_b = bin(input_b)[2:].zfill(32)
        and_gate = And(32, input_a, input_b).get_output()
        assert and_gate == C \
            , f"And: Test case number {self.__index + 1} failed. Expected {C} but got {and_gate}"
    
    
    def __test_or(self):
        C = self.__input_a | self.__input_b
        input_a = self.__input_a
        input_b = self.__input_b
        if input_a < 0:
            input_a = input_a + (1<<32)
        if input_b < 0:
            input_b = input_b + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        input_b = bin(input_b)[2:].zfill(32)
        or_gate = Or(32, input_a, input_b).get_output()
        assert or_gate == C \
            , f"Or: Test case number {self.__index + 1} failed. Expected {C} but got {or_gate}"
    
    
    def __test_nor(self):
        C = ~(self.__input_a | self.__input_b)
        input_a = self.__input_a
        input_b = self.__input_b
        if input_a < 0:
            input_a = input_a + (1<<32)
        if input_b < 0:
            input_b = input_b + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        input_b = bin(input_b)[2:].zfill(32)
        nor_gate = Nor(32, input_a, input_b).get_output()
        assert nor_gate == C \
            , f"Nor: Test case number {self.__index + 1} failed. Expected {C} but got {nor_gate}"
    
    
    def __test_xor(self):
        C = self.__input_a ^ self.__input_b
        input_a = self.__input_a
        input_b = self.__input_b
        if input_a < 0:
            input_a = input_a + (1<<32)
        if input_b < 0:
            input_b = input_b + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        input_b = bin(input_b)[2:].zfill(32)
        xor_gate = Xor(32, input_a, input_b).get_output()
        assert xor_gate == C \
            , f"Xor: Test case number {self.__index + 1} failed. Expected {C} but got {xor_gate}"
    
    
    def __test_not(self):
        C = ~self.__input_a
        input_a = self.__input_a
        if input_a < 0:
            input_a = input_a + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        not_gate = Not(32, input_a).get_output()
        assert not_gate == C \
            , f"Not: Test case number {self.__index + 1} failed. Expected {C} but got {not_gate}"
            
    
    def __test_xnor(self):
        C = ~(self.__input_a | self.__input_b)
        input_a = self.__input_a
        input_b = self.__input_b
        if input_a < 0:
            input_a = input_a + (1<<32)
        if input_b < 0:
            input_b = input_b + (1<<32)
        if C < 0:
            C = C + (1<<32)
        C = bin(C)[2:].zfill(32)
        input_a = bin(input_a)[2:].zfill(32)
        input_b = bin(input_b)[2:].zfill(32)
        xnor_gate = Xnor(32, input_a, input_b).get_output()
        assert xnor_gate == C \
            , f"Xnor: Test case number {self.__index + 1} failed. Expected {C} but got {xnor_gate}"
    
    