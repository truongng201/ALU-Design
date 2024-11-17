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

A = bin(A)[2:].zfill(32)
B = bin(B)[2:].zfill(32)
Op = bin(Op)[2:].zfill(4)
C = bin(C)[2:].zfill(32)
V = bin(V)[2:].zfill(1)

adder = AddSub32Block(A, B, Op)

assert adder.get_output() == C
assert adder.get_overflow() == V