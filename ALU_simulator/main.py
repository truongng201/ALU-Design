# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

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