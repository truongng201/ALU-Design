import random
import os 

MIN_INT = -2**31
MAX_INT = 2**31-1
MOD = 2**32
CARRY_VALUES = [0, 1]
TOTAL_SHIFT_AMOUNT = 32

# check if folder exists
if not os.path.exists("../Test_Vector"):
    os.makedirs("../Test_Vector")

# check if file exists
if os.path.exists(os.path.join("Test_Vector", "LeftShift32_test_vector.txt")):
    os.remove(os.path.join("Test_Vector", "LeftShift32_test_vector.txt"))

# open file
file = open(os.path.join("Test_Vector", "LeftShift32_test_vector.txt"), "a")
# write header
file.write("B[32] Sa[5] Cin C[32]\n")

file.write("#Edge cases\n")
# B is MAX_INT
file.write("#B is max\n")
for Sa in range(TOTAL_SHIFT_AMOUNT):
    for Cin in CARRY_VALUES:
        B = MAX_INT
        C = B << Sa
        if Cin == 1:
            C += 2**Sa - 1
        if C > MAX_INT or C < MIN_INT:
            C = C % MOD
        file.write(f"{B} {Sa} {Cin} {C}\n")

# B is MIN_INT
file.write("#B is min\n")
for Sa in range(TOTAL_SHIFT_AMOUNT):
    for Cin in CARRY_VALUES:
        B = MIN_INT
        C = B << Sa
        if Cin == 1:
            C += 2**Sa - 1
        if C > MAX_INT or C < MIN_INT:
            C = C % MOD
        file.write(f"{B} {Sa} {Cin} {C}\n")
  

file.write("#Random cases\n")
for i in range(3000):
    B = random.randint(MIN_INT, MAX_INT)
    Sa = random.randint(0, 31)
    Cin = random.randint(0, 1)
    C = B << Sa
    if Cin == 1:
        C += 2**Sa - 1
    if C > MAX_INT or C < MIN_INT:
        C = C % MOD
    file.write(f"{B} {Sa} {Cin} {C}\n")
