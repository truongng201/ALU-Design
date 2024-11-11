import random
import os 

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

for i in range(10000):
    B = random.randint(-2**31, 2**31-1)
    Sa = random.randint(0, 31)
    Cin = random.randint(0, 1)
    C = B << Sa
    if Cin == 1:
        C += 2**Sa - 1
    if C > 2**31-1 or C < -2**31:
        C = C % 2**32
    file.write(f"{B} {Sa} {Cin} {C}\n")
