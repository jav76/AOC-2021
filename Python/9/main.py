
def getInput(file="input.txt"):
    grid = []
    with open(file, mode="r") as f:
        lines = f.readlines()
        for i in lines:
            newRow = []
            for nums in i.strip():
                newRow.append(int(nums))
            grid.append(newRow)
    return grid


def part1(input):
    lowPoints = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            lowPoint = True
            currentPos = input[y][x]

            if y > 0: # Check up
                if input[y - 1][x] <= currentPos:
                    lowPoint = False

            if y < len(input) - 1: # Check down
                if input[y + 1][x] <= currentPos:
                    lowPoint = False

            if x < len(input[0]) - 1: # Check Right
                if input[y][x + 1] <= currentPos:
                    lowPoint = False

            if x > 0: # Check Left
                if input[y][x - 1] <= currentPos:
                    lowPoint = False

            if lowPoint:
                lowPoint = (x, y, currentPos)
                lowPoints.append(lowPoint)


    sum = 0
    for i in lowPoints:
        sum += i[2] + 1
    print(sum)
    512


if __name__ == '__main__':
    input = getInput()
    part1(input)

