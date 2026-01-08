#aqui automatizei a criação dos 3 tipos de vetores diferente que o rai pediu
import random

def generate_ascending(n):
    return list(range(n))

def generate_descending(n):
    return list(range(n, 0, -1))

def generate_random(n):
    return random.sample(range(n), n)  # sem repetição
