# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

from ALU_simulator.Test.TestALU32 import TestALU32

print("-" * 50)
print("--------- ALU32: Starting test cases ------------")
print("-" * 50)
TestALU32()
print("-" * 50)
print("----------------- End test cases ----------------")
print("-" * 50)