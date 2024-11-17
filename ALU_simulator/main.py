# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

import random
from ALU_simulator.Adders.AddSub32Block import AddSub32Block

MAX_INT = 2**31 - 1
MIN_INT = - 2**31
MOD = 2**32

A = random.randint(-2**31, 2**31-1)
B = random.randint(-2**31, 2**31-1)
Op = random.choice([2, 3, 6, 7])

if Op == 2 or Op == 3:
    C = A + B
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    else:
        V = 0
elif Op == 6 or Op == 7:
    C = A - B
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    else:
        V = 0


if A < 0:
    A = bin(A)[3:].zfill(32)
else:
    A = bin(A)[2:].zfill(32)
    
if B < 0:
    B = bin(B)[3:].zfill(32)
else:
    B = bin(B)[2:].zfill(32)
if C < 0:
    C = bin(C)[3:].zfill(32)
else:
    C = bin(C)[2:].zfill(32)
Op = bin(Op)[2:].zfill(4)
adder = AddSub32Block(A, B, Op)


print(adder.get_output())
print(C)
assert adder.get_output() == C
assert adder.get_overflow() == V