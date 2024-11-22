from ALU_simulator.Comparators import LessThanOrEqual0

class TestLessThanOrEqual0:
    def __init__(self):
        assert LessThanOrEqual0("0" * 32).get_output() == "1" \
            , "LessThanOrEqual0: Test case 1 failed"
        assert LessThanOrEqual0("1" * 32).get_output() == "1" \
            , "LessThanOrEqual0: Test case 2 failed"
        assert LessThanOrEqual0("0" + "0110101010101001010101101010000").get_output() == "0" \
            , "LessThanOrEqual0: Test case 3 failed"
        assert LessThanOrEqual0("1" + "0110101010101001010101101010000").get_output() == "1" \
            , "LessThanOrEqual0: Test case 4 failed"
        print("LessThanOrEqual0: All test cases pass")