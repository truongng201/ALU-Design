import random
import os  

# check if folder exists
if not os.path.exists("Test_Vector"):
    os.makedirs("Test_Vector")

# check if file exists
if os.path.exists(os.path.join("Test_Vector", "Add32_test_vector.txt")):
    os.remove(os.path.join("Test_Vector", "Add32_test_vector.txt"))

# open file
file = open(os.path.join("Test_Vector", "Add32_test_vector.txt"), "a")
# write header
file.write("A[32] B[32] Cin C[32] V\n")

for i in range(10000):
    A = random.randint(-2**31, 2**31-1)
    B = random.randint(-2**31, 2**31-1)
    Cin = random.randint(0, 1)
    C = A + B + Cin
    V = 0
    if C > 2**31-1 or C < -2**31:
        C = C % 2**32
        V = 1
    
        
    file.write(f"{A} {B} {Cin} {C} {V}\n")