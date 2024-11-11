class FlipMirror32bit:
    def __init__(self, input: str):
        self.input = input
        self.__output = input[::-1]

    def get_output(self) -> str:
        return self.output