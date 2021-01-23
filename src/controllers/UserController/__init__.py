import math
from random import random


class UtilsHelper:
    @staticmethod
    def generate_unique_hash():
        def s4():
            result = str(math.floor((1 + random()) * 0x10000))
            return result[1:]
        return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()