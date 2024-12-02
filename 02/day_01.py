from typing import List
import numpy as np

def p1(input: List[str]) -> int:
    safe = 0
    for row in input:
        numbers = [int(x) for x in row.split()]
        if isValid(numbers):
            safe += 1
    return safe
           

def p2(input: List[str]) -> int:
    safe = 0
    for row in input:
        numbers = [int(x) for x in row.split()]
        if isValid(numbers):
            safe += 1
            continue

        for i in range(len(numbers)):
            copy = numbers.copy()
            copy.pop(i)
            if isValid(copy):
                safe += 1 
                break

    return safe

def isValid(numbers):
    return isSorted(numbers) and isDifferenceBetweenOneAndThree(numbers)

def isSorted(numbers):
    return numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)


def isDifferenceBetweenOneAndThree(numbers):
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        current = numbers[i]
        next = numbers[i+1]
        diff = abs(current - next)
        if diff < 1 or diff > 3:
            return False
    return True

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    input = read_file("02/input.txt")
    print(p1(input))
    print(p2(input))

