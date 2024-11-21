import random
import os  


MAX_INT = 2**31-1
MIN_INT = -2**31
MOD = 2**32
CARRY_VALUES = [0, 1]

# check if folder exists
if not os.path.exists("../Test_Vector"):
    os.makedirs("../Test_Vector")

# check if file exists
if os.path.exists(os.path.join("Test_Vector", "Add32_test_vector.txt")):
    os.remove(os.path.join("Test_Vector", "Add32_test_vector.txt"))

# open file
file = open(os.path.join("Test_Vector", "Add32_test_vector.txt"), "a")
# write header
file.write("A[32] B[32] Cin C[32] V\n")

file.write("#Edge cases\n")
# Both A and B are MAX_INT
for Cin in CARRY_VALUES:
    A = MAX_INT
    B = MAX_INT
    C = A + B + Cin
    V = 0
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    file.write(f"{A} {B} {Cin} {C} {V}\n")

# Both A and B are MIN_INT
file.write("#Both A and B are min\n")
for Cin in CARRY_VALUES:
    A = MIN_INT
    B = MIN_INT
    C = A + B + Cin
    V = 0
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    file.write(f"{A} {B} {Cin} {C} {V}\n")


# A is MAX_INT and B is MIN_INT
file.write("#A is max and B is min\n")
for Cin in CARRY_VALUES:
    A = MAX_INT
    B = MIN_INT
    C = A + B + Cin
    V = 0
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    file.write(f"{A} {B} {Cin} {C} {V}\n")

# A is MIN_INT and B is MAX_INT
file.write("#A is min and B is max\n")
for Cin in CARRY_VALUES:
    A = MIN_INT
    B = MAX_INT
    C = A + B + Cin
    V = 0
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
    file.write(f"{A} {B} {Cin} {C} {V}\n")

file.write("#Random cases\n")
for i in range(3000):
    A = random.randint(MIN_INT, MAX_INT)
    B = random.randint(MIN_INT, MAX_INT)
    Cin = random.randint(0, 1)
    C = A + B + Cin
    V = 0
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
        V = 1
        
    file.write(f"{A} {B} {Cin} {C} {V}\n")