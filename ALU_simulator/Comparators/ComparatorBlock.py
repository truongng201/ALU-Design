class ComparatorBlock:
    def __init__(self, comparator):
        self.comparator = comparator

    def compare(self, a, b):
        return self.comparator.compare(a, b)