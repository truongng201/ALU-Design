import random
import os

MAX_INT = 2**31 - 1
MIN_INT = - 2**31
MOD = 2**32
TOTAL_OP_CODE = 16
TOTAL_SHIFT_AMOUNT = 32

# check if folder exists
if not os.path.exists("../Test_Vector"):
	os.makedirs("../Test_Vector")

# check if file exists
if os.path.exists(os.path.join("Test_Vector", "ALU32_test_vector.txt")):
	os.remove(os.path.join("Test_Vector", "ALU32_test_vector.txt"))

# open file
file = open(os.path.join("Test_Vector", "ALU32_test_vector.txt"), "a")
# write header
file.write('A[32] B[32] Op[4] Sa[5] C[32] V\n')

def get_result(input_a, input_b, op_code, shift_amount):
    output_c = None
    overflow_v = 0
    # Shift left logical
    if op_code == 0 or op_code == 1:
        output_c = input_b << shift_amount
        if output_c > MAX_INT or output_c < MIN_INT:
            output_c = output_c % MOD
        return output_c, overflow_v
    
    # Add operation
    if op_code == 2 or op_code == 3:
        output_c = input_a + input_b
        if output_c > MAX_INT or output_c < MIN_INT:
            output_c = output_c % MOD
            overflow_v = 1
        return output_c, overflow_v
    
    # And operation
    if op_code == 4:
        output_c = input_a & input_b
        return output_c, overflow_v

    # Or operation
    if op_code == 5:
        output_c = input_a | input_b
        return output_c, overflow_v
    
    # Subtract operation
    if op_code == 6 or op_code == 7:
        output_c = input_a - input_b
        if output_c > MAX_INT or output_c < MIN_INT:
            output_c = output_c % MOD
            overflow_v = 1
        return output_c, overflow_v
    
    # Not equal operation
    if op_code == 8:
        output_c = 1 if input_a != input_b else 0
        return output_c, overflow_v
    
    # Equal operation
    if op_code == 9:
        output_c = 1 if input_a == input_b else 0
        return output_c, overflow_v

    
    # Xor operation
    if op_code == 10:
        output_c = input_a ^ input_b
        return output_c, overflow_v
    
    # Nor operation
    if op_code == 11:
        output_c = ~(input_a | input_b)
        return output_c, overflow_v

    # Shift right logical operation
    if op_code == 12:
        if input_b < 0:
            input_b = input_b + MOD
        output_c = input_b >> shift_amount	
        return output_c, overflow_v
    
    # Shift right arithmetic operation
    if op_code == 13:
        output_c = input_b >> shift_amount
        if output_c > MAX_INT or output_c < MIN_INT:
            output_c = output_c % MOD
        return output_c, overflow_v
    
    # A less than or equal to zero
    if op_code == 14:
        output_c = 1 if input_a <= 0 else 0
        return output_c, overflow_v
    
    # A greater than zero
    if op_code == 15:
        output_c = 1 if input_a > 0 else 0
        return output_c, overflow_v
    
    return None, None

def generate_edge_cases():
    file.write("# Edge cases\n")
    
    A, B = None, None
    
    # both A and B is 0
    for Op in range(TOTAL_OP_CODE):
        A = 0
        B = 0
        
        for Sa in range(TOTAL_SHIFT_AMOUNT):
            output_c, overflow_v = get_result(input_a=A, input_b=B, op_code=Op, shift_amount=Sa)
            if output_c == None or overflow_v == None:
                print("generate_edge_cases.case1: Something wrong")
                return
            file.write(f"{A} {B} {Op} {Sa} {output_c} {overflow_v}\n")
        

    # A is 0 and B is max
    for Op in range(TOTAL_OP_CODE):
        A = 0
        B = MAX_INT
        
        for Sa in range(TOTAL_SHIFT_AMOUNT):
            output_c, overflow_v = get_result(input_a=A, input_b=B, op_code=Op, shift_amount=Sa)
            if output_c == None or overflow_v == None:
                print("generate_edge_cases.case2: Something wrong")
                return
            file.write(f"{A} {B} {Op} {Sa} {output_c} {overflow_v}\n")
            
    # A is max and B is max
    for Op in range(TOTAL_OP_CODE):
        A = MAX_INT
        B = MAX_INT
        
        for Sa in range(TOTAL_SHIFT_AMOUNT):
            output_c, overflow_v = get_result(input_a=A, input_b=B, op_code=Op, shift_amount=Sa)
            if output_c == None or overflow_v == None:
                print("generate_edge_cases.case3: Something wrong")
                return
            file.write(f"{A} {B} {Op} {Sa} {output_c} {overflow_v}\n")
    
    # A is min and B is min
    for Op in range(TOTAL_OP_CODE):
        A = MIN_INT
        B = MIN_INT
        
        for Sa in range(TOTAL_SHIFT_AMOUNT):
            output_c, overflow_v = get_result(input_a=A, input_b=B, op_code=Op, shift_amount=Sa)
            if output_c == None or overflow_v == None:
                print("generate_edge_cases.case4: Something wrong")
                return
            file.write(f"{A} {B} {Op} {Sa} {output_c} {overflow_v}\n")
    
 
def generate_random_cases(number_of_cases = 10000):
    file.write("# Random cases\n")
    for _ in range(number_of_cases):
        A = random.randint(MIN_INT, MAX_INT)
        B = random.randint(MIN_INT, MAX_INT)
        Op = random.randint(0, 15)
        Sa = random.randint(0, 31)
        output_c, overflow_v = get_result(input_a=A, input_b=B, op_code=Op, shift_amount=Sa)
        if output_c == None or overflow_v == None:
            print("generate_random_cases: Something wrong")
            return
        
        file.write(f"{A} {B} {Op} {Sa} {output_c} {overflow_v}\n")
        
generate_edge_cases()
generate_random_cases()