from ALU_simulator.Comparators import BitExtend1to32

class TestBitExtend1to32:
    def __init__(self):
        assert BitExtend1to32("1").get_output() == "0" * 31 + "1" \
            , "BitExtend1to32: Test case 1 failed"
        assert BitExtend1to32("0").get_output() == "0" * 32 \
            , "BitExtend1to32: Test case 2 failed"
        print("BitExtend1to32: All test cases pass")