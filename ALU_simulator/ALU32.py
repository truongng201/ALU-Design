class ALU32:
    def __init__(self):
        self.result = 0
        self.blocks = []
        
    def add_block(self, block):
        self.blocks.append(block)
        