from typing import List

def p1(input: List[str]) -> int:
    first_column = [int(x.split()[0]) for x in input]
    second_column = [int(x.split()[1]) for x in input]

    diff = 0
    for i in range(len(first_column)):
        # get the smallest number in the first column
        min_first = min(first_column)
        # get the smallest number in the second column
        min_second = min(second_column)
        diff += abs(min_first - min_second)
        # remove the smallest number in the first column
        first_column.remove(min_first)
        # remove the smallest number in the second column
        second_column.remove(min_second)

    return diff

def p2(input: List[str]) -> int:
    first_column = [int(x.split()[0]) for x in input]
    second_column = [int(x.split()[1]) for x in input]

    diff = 0
    for i in range(len(first_column)):
        number = first_column[i]
        similar = second_column.count(number)
        diff += (similar * number)
    return diff

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    input = read_file("01/input.txt")
    print(p1(input))
    print(p2(input))

