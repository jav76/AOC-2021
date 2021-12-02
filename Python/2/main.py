

def getInput(file="input.txt"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

def solution1(input):
    position = 0
    depth = 0
    for i in input:
        dir, num = i.split()
        num = int(num)
        match dir:
            case "forward":
                position += num
            case "down":
                depth += num
            case "up":
                depth -= num
    return position * depth

def solution2(input):
    aim = 0
    position = 0
    depth = 0
    for i in input:
        dir, num = i.split()
        num = int(num)
        match dir:
            case "forward":
                position += num
                depth += aim * num
            case "down":
                aim += num
            case "up":
                aim -= num
    return position * depth

def getOutput(output, file="output.txt"):
    with open(file, "w") as f:
        f.write(
            f"Position * depth 1: {output[0]}\n"
            f"Position * depth 2: {output[1]}"
        )

if __name__ == '__main__':
    input = getInput()
    output1 = solution1(input)
    output2 = solution2(input)
    getOutput((output1, output2))
    #(1924923, 1982495697)
