import statistics, math

def getInput(file="input.txt"):
    with open(file, "r") as f:
        vals = f.read()
        nums = [int(i) for i in vals.split(",")]
        return nums

def part1(input):
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14] test case
    med = int(statistics.median(input))
    fuel = 0
    for i in input:
        fuel += abs(i - med)
    print(fuel)
    # 349769

def part2(input):
    # input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14] test case
    avg = sum(input) / len(input)
    avg = int(math.floor(avg))
    fuel = 0
    for i in input:
        fuel += sum(range(abs(i - avg) + 1))
    print(fuel)
    # 99540554


if __name__ == '__main__':
    input = getInput()
    output = part1(input)
    output = part2(input)
