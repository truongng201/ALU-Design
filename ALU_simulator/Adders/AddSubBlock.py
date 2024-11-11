class AddSubBlock:
    def __init__(self):
        self.adder = None
        self.subtractor = None
        
    def add(self, a, b):
        return self.adder.add(a, b)

    def sub(self, a, b):
        return self.subtractor.sub(a, b)