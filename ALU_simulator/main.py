# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

import sys

from ALU_simulator.ALU32 import ALU32

# read the input arguments from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]

out_file = open(output_file, "w")
out_file.write("C[32] V\n")
with open(input_file, "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0:
            continue
        A, B, Op, Sa = map(int, line.split(" "))

        if A < 0:
            A = A + 2**32
        if B < 0:
            B = B + 2**32
        
        A = bin(A)[2:].zfill(32)
        B = bin(B)[2:].zfill(32)
        Op = bin(Op)[2:].zfill(4)
        Sa = bin(Sa)[2:].zfill(5)
        
        alu = ALU32(A, B, Op, Sa)
        alu_output = alu.get_output()
        alu_overflow = alu.get_overflow()
        out_file.write(f"{alu_output} {alu_overflow}\n")
        
out_file.close()