class Manager:
    def __init__(self) -> None:
        self.stack = []

    def push(self, bytes: bytes):
        self.stack.append(bytes)

    def pop(self, byte_count = 1):
        if byte_count == 1: return self.stack.pop()
        else:
            result = []
            for _ in range(byte_count):
                result.append(self.stack.pop())
            return result