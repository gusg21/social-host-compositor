import math
import random


class StringFactory:
    def __init__(self, mash_iter_count = 10) -> None:
        self.data = ""
        self.mash_iter_count = mash_iter_count

    def append(self, string: str | bytes):
        if string is str:
            self.data += string
        elif string is bytes:
            self.data += str(string)

    def build(self, build_parameters: dict):
        processed_data = self.data
        if build_parameters["reverse"]:
            processed_data = reversed(self.data)
        if build_parameters["mash"]:
            for _ in range(self.mash_iter_count):
                data_len = len(processed_data)
                processed_data[random.randint(0, data_len - 1)]
        return self.data[0:]