

def getInput(file="input.txt"):
    with open(file, "r") as f:
        lines = f.read()
        nums = [int(i) for i in lines.splitlines()]
        return nums

def solution(input):
    larger = 0
    lastMeasurement = input[0]
    largerWindows = 0
    for i in range(0, len(input)):
        if input[i] > lastMeasurement:
            larger += 1
        lastMeasurement = input[i]

        if i < len(input) - 3:
            currentWindow = sum(input[i:i+3])
            nextWindow = sum(input[i+1:i+4])
            if nextWindow > currentWindow:
                largerWindows += 1

    return larger, largerWindows

def getOutput(output, file="output.txt"):
    with open(file, "w") as f:
        f.write(
            f"Larger measurements: {output[0]}\n"
            f"Larger sums: {output[1]}"
        )

if __name__ == '__main__':
    input = getInput()
    output = solution(input)
    print(output)
    getOutput(output)
    #(1462, 1497)