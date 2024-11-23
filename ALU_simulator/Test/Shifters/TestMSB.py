from ALU_simulator.Shifters import MSB

class TestMSB:
    def __init__(self):
        assert MSB("0" * 32).get_output() == "0" \
            , "MSB: Test case 1 failed"
        assert MSB("1" * 32).get_output() == "1" \
            , "MSB: Test case 2 failed"
        assert MSB("0" + "1" * 31).get_output() == "0" \
            , "MSB: Test case 3 failed"
        assert MSB("1" + "0" * 31).get_output() == "1" \
            , "MSB: Test case 4 failed"
        print("MSB: All test cases pass")