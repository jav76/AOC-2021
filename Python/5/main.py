def getInput(file="input.txt"):
    with open(file, "r") as f:
        lines = f.read()
        lines = lines.splitlines()
        points = [[],[]]
        for i in lines:
            x1Pos = i.find(",")
            y1Pos = i.find("->")
            x1 = int(i[:x1Pos])
            y1 = int(i[x1Pos + 1:y1Pos])
            x2Pos = i.find(",", y1Pos)
            x2 = int(i[y1Pos + 2:x2Pos])
            y2 = int(i[x2Pos + 1:])
            point1 = (x1, y1)
            point2 = (x2, y2)
            points[0].append(point1)
            points[1].append(point2)
    return points

def part1(input):
    overlaps = {}
    for i in range(len(input[0])):
        x1 = input[0][i][0]
        x2 = input[1][i][0]
        y1 = input[0][i][1]
        y2 = input[1][i][1]
        if x1 == x2 or y1 == y2:
            if x1 < x2:
                xVals = range(x1, x2 + 1)
            else:
                xVals = range(x1, x2 - 1, -1)
            if y1 < y2:
                yVals = range(y1, y2 + 1)
            else:
                yVals = range(y1, y2 - 1, -1)

            for x in xVals:
                for y in yVals:
                    overlaps[(x, y)] = overlaps.get((x, y), 0) + 1
    totalOverlaps = 0
    for point in overlaps:
        if overlaps[point] >= 2:
            totalOverlaps += 1
    print(totalOverlaps)
    #4655

def part2(input):
    overlaps = {}
    for i in range(len(input[0])):
        x1 = input[0][i][0]
        x2 = input[1][i][0]
        y1 = input[0][i][1]
        y2 = input[1][i][1]
        if x1 < x2:
            xVals = range(x1, x2 + 1)
        else:
            xVals = range(x1, x2 - 1, -1)
        if y1 < y2:
            yVals = range(y1, y2 + 1)
        else:
            yVals = range(y1, y2 - 1, -1)

        if x1 == x2 or y1 == y2:
            for x in xVals:
                for y in yVals:
                    overlaps[(x, y)] = overlaps.get((x, y), 0) + 1
        else:
            for point in zip(xVals, yVals):
                overlaps[point] = overlaps.get(point, 0) + 1
    totalOverlaps = 0
    for point in overlaps:
        if overlaps[point] >= 2:
            totalOverlaps += 1
    print(totalOverlaps)
    #20500


if __name__ == '__main__':
    input = getInput()
    output = part1(input)
    output = part2(input)
