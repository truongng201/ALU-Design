# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

from ALU_simulator.Test.Adders import *
from ALU_simulator.Test.Comparators import *

try:
    TestAdder1bit()
    TestAdder4bitOverflow()
    TestAdder16bitOverflow()
    TestAdder32bitOverflow()
    # TestAddSub32Block()
    
    TestIsEqual0()
    TestBitExtend1to32()
    TestIsEqual()
except AssertionError as e:
    print(e)
    print("Test failed")