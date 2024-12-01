import math
import random

def degrees_to_radians(degrees):
    return degrees * math.pi / 180.0

def random_range(min, max):
    return min + (max - min) * random.random()