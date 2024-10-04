import math
import random

def lcm(a, b, c):
    ab_lcm = abs(a * b) // math.gcd(a, b)
    return abs(ab_lcm * c) // math.gcd(ab_lcm, c)

def generate_numbers():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    third_number = random.randint(1, 100)
    question = f"{first_number} {second_number} {third_number}"
    correct_answer = str(lcm(first_number, second_number, third_number))

    return question, correct_answer
