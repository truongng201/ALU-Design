from ALU_simulator.Comparators import IsEqual0

class TestIsEqual0:
    def __init__(self):
        assert IsEqual0("0" * 32).get_output() == "1" \
            , "IsEqual0: Test case 1 failed"
        assert IsEqual0("1" * 32).get_output() == "0" \
            , "IsEqual0: Test case 2 failed"
        assert IsEqual0("0" * 31 + "1").get_output() == "0" \
            , "IsEqual0: Test case 3 failed"
        print("IsEqual0: All test cases pass")