import time
def getInput(file="input.txt"):
    with open(file, "r") as f:
        vals = f.read()
        nums = [int(i) for i in vals.split(",")]
        return nums

def solution(input, days):
    fishDict = {x:0 for x in range(0, 9)}
    # Initial conditions
    for i in input:
        fishDict[i] += 1
    # Update
    for t in range(days):
        newFish = fishDict[0]
        fishDict[0] = fishDict[1]
        for key, val in fishDict.items():
            if key != 0 and key != 8:
                fishDict[key] = fishDict[key + 1]

        fishDict[8] = newFish
        fishDict[6] += newFish
        #print(f"Fish after day {t}: {sum(fishDict.values())}")
    return sum(fishDict.values())

if __name__ == '__main__':
    input = getInput()
    print(solution(input, 80))
    print(solution(input, 256))
    start = time.time()
    print(solution(input, 1000000))
    print(abs(start - time.time()))





