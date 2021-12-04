import copy
def getInput(file="input.txt"):
    with open(file, "r") as f:
        lines = f.read()
        return lines.splitlines()

def commonBits(input):
    sums = [0] * len(input[0])
    for i in input:
        for j in range(len(sums)):
            sums[j] += int(i[j])
    bits = [0] * len(sums)
    for i in range(len(sums)):
        bits[i] = sums[i] / len(input)

    return bits

def part1(input):
    # powerConsumption = gamma * epsilon
    bits = commonBits(input)
    gammaRate = ""
    epsilonRate = ""
    for i in bits:
        if i >= 0.5:
            gammaRate += "1"
            epsilonRate += "0"
        else:
            gammaRate += "0"
            epsilonRate += "1"
    powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)
    return powerConsumption
    # 2967914

def part2(input):
    # lifeSupportRating = Oxygen generator rating * C02 scrubber rating
    oxygenRating = copy.deepcopy(input)
    CO2Rating = copy.deepcopy(input)
    n = 0
    while len(oxygenRating) > 1:
        bits = commonBits(oxygenRating)
        for i in oxygenRating[:]:
            bit = 0
            if bits[n] >= 0.5:
                bit = 1
            if int(i[n]) != bit:
                oxygenRating.remove(i)
                if len(oxygenRating) == 1:
                    break
        n += 1
        print(oxygenRating)
    n = 0
    while len(CO2Rating) > 1:
        bits = commonBits(CO2Rating)
        for i in CO2Rating[:]:
            bit = 1
            if bits[n] >= 0.5:
                bit = 0
            if int(i[n]) != bit:
                CO2Rating.remove(i)
                if len(CO2Rating) == 1:
                    break
        n += 1
        print(CO2Rating)
    oxygenRating = oxygenRating[0]
    CO2Rating = CO2Rating[0]
    print(int(oxygenRating, 2))
    print(int(CO2Rating, 2))
    lifeRating = int(oxygenRating, 2) * int(CO2Rating, 2)
    return lifeRating

if __name__ == '__main__':
    input = getInput()
    #output = part1(input)
    output = part2(input)
    print(output)
