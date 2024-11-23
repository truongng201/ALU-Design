# Simple ALU for course COMP2020 - computer organization

## Project overview

This is a simple ALU for course COMP2020 - computer organization. It is implemented in Verilog. The ALU supports the following operations:

### Supported operations table

| Op   | name                   | C                                      | V            |
| ---- | ---------------------- | -------------------------------------- | ------------ |
| 0100 | and                    | C = A & B                              | V = 0        |
| 0101 | or                     | C = A \| B                             | V = 0        |
| 000x | shift left logical     | C = B << Sa                            | V = 0        |
| 1010 | xor                    | C = A ^ B                              | V = 0        |
| 1011 | nor                    | C = ~(A \| B)                          | V = 0        |
| 1100 | shift right logical    | C = B >>> Sa                           | V = 0        |
| 1101 | shift right arithmetic | C = B >> Sa                            | V = 0        |
| 1000 | ne                     | C = (A != B) ? 000...0001 : 000...0000 | V = 0        |
| 1001 | eq                     | C = (A == B) ? 000...0001 : 000...0000 | V = 0        |
| 1110 | le                     | C = (A ≤ 0) ? 000...0001 : 000...0000  | V = 0        |
| 1111 | gt                     | C = (A > 0) ? 000...0001 : 000...0000  | V = 0        |
| 011x | subtract               | C = A - B                              | V = overflow |
| 001x | add                    | C = A + B                              | V = overflow |

### Inputs and outputs

#### ALU32

- Operation (4 bits) - op: operation to be performed (0, 15)
- A (32 bits) - input_a: input A
- B (32 bits) - input_b: input B
- Sa (5 bits) - input_sa: shift amount (0, 31)
- C (32 bits) - output_c: output C
- V (1 bit) - output_v: identify overflow or not (0 or 1)

#### ADD32

- A (32 bits) - input_a: input A
- B (32 bits) - input_b: input B
- Cin (1 bit) - input_cin: carry in bit
- C (32 bits) - output_c: output C
- V (1 bit) - output_v: identify overflow or not (0 or 1)

#### Leftshift32

- B (32 bits) - input_b: input B
- Sa (5 bits) - input_sa: shift amount (0, 31)
- Cin (1 bit) - input_cin: carry in
- C (32 bits) - input_c: output C

## ALU Simulation

### Description

The ALU simulation is implemented in Python. The simulation reads the input from a file and writes the output to another file. The input file should contain the following information:

- The first line contains the number of test cases
- Each test case contains the following information:

  - The operation to be performed (4 bits)
  - The input A (32 bits)
  - The input B (32 bits)
  - The shift amount (5 bits)

- The output file contains the following information:
  - The output C (32 bits)
  - The output V (1 bit)

### Usage

First, you need to change directory to the `ALU_simulator` directory and then add the input file and output file to the directory:

```bash
cd ALU_simulator && touch input_file output_file
```

To run the simulation, you need to have Python installed on your machine. You can run the simulation by executing the following command:

```bash
python3 main.py input_file output_file
```

Where `input_file` is the path to the input file and `output_file` is the path to the output file.

To test the ALU, you can use the provided test cases in the `test` directory. You can run the simulation using the following command:

```bash
python3 TestALU.py && python3 TestComponents.py
```

The result of TestALU.py and TestComponents.py should be all passed.

```txt
TestALU32: Total pass:  14608
TestALU32: Total fail:  0
TestALU32: Finish testing
```

```txt
--------------------------------------------------
----- ALU Components: Starting test cases --------
--------------------------------------------------

----------- Gates: Starting test cases -----------
Gates: All test cases pass
----------- Gates: All test cases pass -----------

---------- Adders: Starting test cases -----------
Adder1bit: All test cases passed
Adder4bitOverflow: All test cases passed
Adder16bitOverflow: All test cases passed
Adder32bitOverflow: All test cases passed
AddSub32Block: All test cases passed
---------- Adders: All test cases pass -----------

------- Comparators: Starting test cases ---------
IsEqual0: All test cases pass
BitExtend1to32: All test cases pass
IsEqual: All test cases pass
LessThanOrEqual0: All test cases pass
GreaterThan0: All test cases pass
------- Comparators: All test cases pass ---------

--------- Logical: Starting test cases -----------
Logical32Block: All test cases passed
--------- Logical: All test cases pass -----------

-------- Shifters: Starting test cases -----------
MSB: All test cases pass
LeftShift1: All test cases passed
LeftShift2: All test cases passed
LeftShift4: All test cases passed
LeftShift8: All test cases passed
LeftShift16: All test cases passed
LeftShift32: All test cases passed
Reverse32bit: All test cases passed
Shifter32Block: All test cases passed
--------------------------------------------------
----- ALU Components: All test test cases --------
--------------------------------------------------
```

TestALU.py is used to test the ALU operation, and TestComponents.py is used to test each sub-component of the ALU.

### Example

The input file should look like this (the type of the input should be decimal):

```txt
A[32] B[32] Op[4] Sa[5]
0 0 0 0
0 0 0 1
0 0 0 2
0 0 0 3
0 0 0 4
0 0 0 5
```

The output file should look like this:

```txt
C[32] V
00000000000000000000000000000000 0
00000000000000000000000000000000 0
00000000000000000000000000000000 0
00000000000000000000000000000000 0
00000000000000000000000000000000 0
00000000000000000000000000000000 0
```

This ALU simulation is used to help you understand the ALU operation (if you don't :> ). You can use it to test the ALU operation and verify the correctness of the ALU implementation. If you like it, please give me a star. Thank you!
