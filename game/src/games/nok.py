import math
import random


def lcm(a, b, c):
    # Сначала находим LCM для a и b
    ab_lcm = abs(a * b) // math.gcd(a, b)
    # Затем находим LCM для ab_lcm и c
    return abs(ab_lcm * c) // math.gcd(ab_lcm, c)


def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    question = f"{num1} {num2} {num3}"
    correct_answer = str(lcm(num1, num2, num3))
    return question, correct_answer
