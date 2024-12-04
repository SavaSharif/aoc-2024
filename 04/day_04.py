def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]

def p1(input):
    occurrences = 0
    
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1), 
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    rows = len(input)
    cols = len(input[0])
    for row in range(rows):
        for col in range(cols):
            for x, y in directions:
                word = ""
                for i in range(len("XMAS")):
                    nr, nc = row + i * x, col + i * y
                    if 0 <= nr < rows and 0 <= nc < cols:
                        word += input[nr][nc]
                if word == "XMAS":
                    occurrences += 1
    return occurrences

def p2(input):
    occurrences = 0

    directions = [
        (1, 1), 
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    rows = len(input)
    cols = len(input[0])

    indexes = []
    for row in range(rows):
        for col in range(cols):
            for x, y in directions:
                word = ""
                indices = []
                for i in range(len("MAS")):
                    nr, nc = row + i * x, col + i * y
                    if 0 <= nr < rows and 0 <= nc < cols:
                        indices.append((nr, nc))
                        word += input[nr][nc]
                if word == "MAS":
                    indexes.append(indices)

    for i in range(len(indexes)):
        for j in range(i+1, len(indexes)):
            if indexes[i][1] == indexes[j][1]:
                occurrences += 1

    return occurrences



if __name__ == "__main__":
    input = read_file("04/input.txt")
    print(p1(input))
    print(p2(input))



