"""
Find the bug and fix it.
"""

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
