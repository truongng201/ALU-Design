# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "ALU_simulator"

from ALU_simulator.Test.Adders import *
from ALU_simulator.Test.Comparators import *
from ALU_simulator.Test.Logical import *
from ALU_simulator.Test.Gates import *
from ALU_simulator.Test.Shifters import *

try:
    print("-" * 50)
    print("----- ALU Components: Starting test cases --------")
    print("-" * 50)
    print()
    print("----------- Gates: Starting test cases -----------")
    TestGates()
    print("----------- Gates: All test cases pass -----------")
    print()
    print("---------- Adders: Starting test cases -----------")
    TestAdder1bit()
    TestAdder4bitOverflow()
    TestAdder16bitOverflow()
    TestAdder32bitOverflow()
    TestAddSub32Block()
    print("---------- Adders: All test cases pass -----------")
    print()
    print("------- Comparators: Starting test cases ---------")
    TestIsEqual0()
    TestBitExtend1to32()
    TestIsEqual()
    TestLessThanOrEqual0()
    TestGreaterThan0()
    TestComparator32Block()
    print("------- Comparators: All test cases pass ---------")
    print()
    print("--------- Logical: Starting test cases -----------")
    TestLogical32Block()
    print("--------- Logical: All test cases pass -----------")
    print()
    print("-------- Shifters: Starting test cases -----------")
    TestMSB()
    TestLeftShift1()
    TestLeftShift2()
    TestLeftShift4()
    TestLeftShift8()
    TestLeftShift16()
    TestLeftShift32()
    TestReverse32bit()
    TestShifter32Block()
    print("-" * 50)
    print("----- ALU Components: All test test cases --------")
    print("-" * 50)
except AssertionError as e:
    print(e)
    print("Test failed")