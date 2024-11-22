from ALU_simulator.Comparators import GreaterThan0

class TestGreaterThan0:
    def __init__(self):
        assert GreaterThan0("1" * 32).get_output() == "0" \
            , "GreaterThan0: Test case 1 failed"
        assert GreaterThan0("0" * 32).get_output() == "0" \
            , "GreaterThan0: Test case 2 failed"
        assert GreaterThan0("0" + "0110101010101001010101101010000").get_output() == "1" \
            , "GreaterThan0: Test case 3 failed"
        assert GreaterThan0("1" + "0110101010101001010101101010000").get_output() == "0" \
            , "GreaterThan0: Test case 4 failed"
        print("GreaterThan0: All test cases pass")