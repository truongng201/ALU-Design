class LeftShift2:
    def __init__(self):
        self.output = 0

    def execute(self, input):
        self.output = input << 2
        return self.output

    def __str__(self):
        return "LeftShift2"