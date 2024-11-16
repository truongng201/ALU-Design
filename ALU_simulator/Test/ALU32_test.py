# Read from test vector file
import os
with open(os.path.exists(os.path.join("Test_Vector", "Add32_test_vector.txt")), "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        A, B, Cin, C, V = line.split()
        A = int(A)
        B = int(B)
        Cin = int(Cin)
        C = int(C)
        V = int(V)
        # Do something with the values
        print(A, B, Cin, C, V)