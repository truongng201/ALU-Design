import random
import os

# check if folder exists
if not os.path.exists("Test_Vector"):
	os.makedirs("Test_Vector")

# check if file exists
if os.path.exists(os.path.join("Test_Vector", "ALU32_test_vector.txt")):
	os.remove(os.path.join("Test_Vector", "ALU32_test_vector.txt"))

# open file
file = open(os.path.join("Test_Vector", "ALU32_test_vector.txt"), "a")
# write header
file.write('A[32] B[32] Op[4] Sa[5] C[32] V\n')


for i in range (50000):
	if i < 16:
		A = 0
		B = 0
		Op = i % 16
	elif i < 32:
		A = 2**31-1
		B = 2**31-1
		Op = i % 16
	elif i < 48:
		A = -2**31
		B = -2**31
		Op = i % 16
	else:
		A = random.randint(-2**31, 2**31-1)
		B = random.randint(-2**31, 2**31-1)
		Op = random.randint(0,15)
	Sa = random.randint(0,31)
	V = 0
	if (Op == 0 or Op == 1): #Shift Left Logical
		C = B << Sa
		if C > 2**31 or C < -2**31:
			C = C % 2**32
	elif (Op == 2 or Op == 3): #Add
		C = A + B
		if C > 2**31-1 or C < -2**31:
			C = C % 2**32
			V = 1
	elif (Op == 4): #And
		C= A & B
	elif (Op == 5): #Or
		C= A | B
	elif (Op == 6 or Op == 7): #Subtract
		C = A - B
		if C > 2**31-1 or C < -2**31:
			C = C % 2**32
			V = 1
	elif (Op == 8): #Not Equal
		if(A != B):
			C = 1
		else:
			C = 0
	elif (Op == 9): #Equal
		if (A == B):
			C = 1
		else:
			C = 0
	elif (Op == 10): #Xor
		C = A^B
	elif (Op == 11): #Nor
		C = ~(A | B)
	elif (Op == 12): #Shift Right Logical
		if B < 0:
			B = B + 2**32
		C = B >> Sa				
	elif (Op == 13): #Shift Right Arithmetic
		C = B >> Sa
		if C > 2**31 or C < -2**31:
			C = C % 2**32
	elif (Op == 14): # A Less Than or Equal to Zero	
		if (A <= 0):
			C = 1
		else:
			C = 0
	elif (Op == 15): #A Greater than Zero
		if(A > 0):
			C = 1
		else:
			C = 0
	file.write(f"{A} {B} {Op} {Sa} {C} {V}\n")		