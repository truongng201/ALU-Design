from ALU_simulator.Adders import Adder1bit

class TestAdder1bit:
    def __init__(self):
        assert Adder1bit("0", "0", "0").get_output() == "0" \
            and Adder1bit("0", "0", "0").get_carry_out() == "0" \
            , "Adder1bit: Test case 1 failed"
        assert Adder1bit("0", "0", "1").get_output() == "1" \
            and Adder1bit("0", "0", "1").get_carry_out() == "0" \
            , "Adder1bit: Test case 2 failed"
        assert Adder1bit("0", "1", "0").get_output() == "1" \
            and Adder1bit("0", "1", "0").get_carry_out() == "0" \
            , "Adder1bit: Test case 3 failed"
        assert Adder1bit("0", "1", "1").get_output() == "0" \
            and Adder1bit("0", "1", "1").get_carry_out() == "1" \
            , "Adder1bit: Test case 4 failed"
        assert Adder1bit("1", "0", "0").get_output() == "1" \
            and Adder1bit("1", "0", "0").get_carry_out() == "0" \
            , "Adder1bit: Test case 5 failed"
        assert Adder1bit("1", "0", "1").get_output() == "0" \
            and Adder1bit("1", "0", "1").get_carry_out() == "1" \
            , "Adder1bit: Test case 6 failed"
        assert Adder1bit("1", "1", "0").get_output() == "0" \
            and Adder1bit("1", "1", "0").get_carry_out() == "1" \
            , "Adder1bit: Test case 7 failed"
        assert Adder1bit("1", "1", "1").get_output() == "1" \
            and Adder1bit("1", "1", "1").get_carry_out() == "1" \
            , "Adder1bit: Test case 8 failed"
        
        print("Adder1bit: All test cases passed")
        
        