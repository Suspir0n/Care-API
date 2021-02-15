import math
from random import random

@staticmethod
def generate_unique_hash():
    def s4():
        return str(math.floor((1 + random()) * 0x10000))[1:]
    return s4()