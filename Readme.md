# Simple ALU for course COMP2020 - computer organization

## Description

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

This ALU simulation is used to help you understand the ALU operation (if you don't :> ).
