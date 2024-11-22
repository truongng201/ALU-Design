from ALU_simulator.Comparators.IsEqual import IsEqual

class TestIsEqual:
    def __init__(self):
        assert IsEqual("1" * 32, "1" * 32).get_output() == "1" \
            , "IsEqual: Test case 1 failed"
        assert IsEqual("1" * 32, "0" * 32).get_output() == "0" \
            , "IsEqual: Test case 2 failed"
        assert IsEqual("01010101010101010101010101010101", "10101010101010101010101010101010").get_output() == "0" \
            , "IsEqual: Test case 3 failed"
        assert IsEqual("01010101010101010101010101010101", "01010101010101010101010101010101").get_output() == "1" \
            , "IsEqual: Test case 4 failed"
        print("IsEqual: All test cases pass")