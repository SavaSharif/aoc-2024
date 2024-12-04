import re
from typing import List

def p1(input: List[str]) -> int:
    sum = 0
    for line in input:
        to_mult = re.findall(r'mul\((-?\d+,-?\d+)\)', line)
        for i in to_mult:
            a, b = i.split(",")
            sum += (int(a) * int(b))

    return sum
           

def p2(input: List[str]) -> int:
    # flatten the list
    sum = 0
    line = "".join(input)
    # for line in input:
    line = 'do()' + line + 'do()'
    bla = re.sub('don\'t\(\)?(.*?)do\(\)', '', line, flags=re.DOTALL)
    for i in re.findall(r'mul\((\d{1,3},\d{1,3})\)', bla):
        a, b = i.split(",")
        sum += (int(a) * int(b))
    return sum
           

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    input = read_file("03/input.txt")
    print(p1(input))
    print(p2(input))

