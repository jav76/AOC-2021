import string, time

def getInput(file="input.txt"):
    with open(file, mode="r") as f:
        lines = f.readlines()
        template = lines[0].strip()
        rules = {}
        for i in lines[2:]:
            rules[i[:2]] = i[5:].strip()
        return template, rules

def processStep(polymer, rules):
    pairs = []
    for i in range(len(polymer)):
        pair = polymer[i:i + 2]
        if len(pair) == 2:
            pairs.append(pair)

    inserts = []
    #print(rules)
    for i in pairs:
        for key, val in rules.items():
            if i == key:
                inserted = i[0] + val
                inserts.append(inserted)
    return ''.join(inserts) + polymer[len(polymer) - 1]


def part1(polymer, rules):
    nextPolymer = processStep(polymer, rules)
    for i in range(9):
        #print(nextPolymer)
        start = time.time()
        nextPolymer = processStep(nextPolymer, rules)
        print(i, time.time() - start)


    characterCounts = {}
    chars = string.ascii_uppercase
    for i in chars:
        characterCounts[i] = nextPolymer.count(i)

    characterCounts = {x:y for x, y in characterCounts.items() if y != 0}

    mostCommon = max(characterCounts, key=characterCounts.get)
    leastCommon = min(characterCounts, key=characterCounts.get)
    print(nextPolymer)
    print(characterCounts)
    print(characterCounts[mostCommon] - characterCounts[leastCommon])
    # 3213


if __name__ == '__main__':
    input = getInput()
    part1(input[0], input[1])

