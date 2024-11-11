class LeftShift16:
    def __init__(self):
        self.out = 0

    def execute(self, in1):
        self.out = in1 << 1
        return self.out

    def print_result(self):
        print(f"Result: {self.out}")