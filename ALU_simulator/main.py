# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"
import random
from ALU_simulator.Adders import Adder1bit

# MAX_INT = 2**31 - 1
# MIN_INT = - 2**31
# MOD = 2**32

# A = random.randint(-2**31, 2**31-1)
# B = random.randint(-2**31, 2**31-1)
# Op = 2

# if Op == 2 or Op == 3:
#     C = A + B
#     if C > MAX_INT or C < MIN_INT:
#         C = C % MOD
#         V = 1
#     else:
#         V = 0
# elif Op == 6 or Op == 7:
#     C = A - B
#     if C > MAX_INT or C < MIN_INT:
#         C = C % MOD
#         V = 1
#     else:
#         V = 0


# if A < 0:
#     A = bin(A)[3:].zfill(32)
# else:
#     A = bin(A)[2:].zfill(32)
    
# if B < 0:
#     B = bin(B)[3:].zfill(32)
# else:
#     B = bin(B)[2:].zfill(32)
# if C < 0:
#     C = bin(C)[3:].zfill(32)
# else:
#     C = bin(C)[2:].zfill(32)
# Op = bin(Op)[2:].zfill(4)
# adder = Adder32bitOverflow(A, B, "0")


# print("Final result",adder.get_output())
# print("Expec result",C)
# if adder.get_output() == C:
#     print("Test passed")
# else:
#     print("Test failed")


from ALU_simulator.Test.Adders import *

try:
    TestAdder1bit()
    TestAdder4bitOverflow()
    TestAdder16bitOverflow()
    TestAdder32bitOverflow()
    TestAddSub32Block()
except AssertionError as e:
    print(e)
    print("Test failed")