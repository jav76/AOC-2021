def getInput(file="input.txt"):
    with open(file, "r") as f:
        lines = f.read()
        lines = lines.splitlines()
        drawnNumbers = lines[0]
        drawnNumbers = drawnNumbers.split(",")
        drawnNumbers = [int(i) for i in drawnNumbers]
        boards = []
        for i in range(2, len(lines), 6):
            currentBoard = []
            for j in range(0, 5):
                currentBoard.append(lines[i + j].split())
            boards.append(currentBoard)
        return boards, drawnNumbers

def checkBoard(board, nums):
    for row in range(len(board)):
        rowBingo = [False] * len(board)
        colBingo = [False] * len(board)
        for col in range(len(board[row])):
            #print(board[row][col])
            #print(board[col][row])
            if int(board[row][col]) in nums:
                rowBingo[col] = True
            if int(board[col][row]) in nums:
                colBingo[col] = True
        if all(rowBingo) or all(colBingo):
            return all(rowBingo) or all(colBingo)
    return False

def sumBoard(board, nums):
    sum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if int(board[row][col]) not in nums:
                sum += int(board[row][col])
    return sum

def part1(boards, nums):
    calledNums = []
    for i in nums:
        calledNums.append(i)
        for j in boards:
            bingo = checkBoard(j, calledNums)
            if bingo:
                print(f"Board {j} won on number {i}!!!!")
                score = sumBoard(j, calledNums)
                print(score * i)
                return score * i
        print(f"No winners after {i} was called")
        print(calledNums)
        #11536

def part2(boards, nums):
    calledNums = []
    wonBoards = []
    lastNumber = 0
    for i in nums:
        calledNums.append(i)
        for j in boards:
            bingo = checkBoard(j, calledNums)
            if bingo:
                if j not in wonBoards:
                    #print(f"Board {j} won on number {i}!!!!")
                    wonBoards.append(j)
                    lastNumber = i
    newCalledNums = []
    for i in calledNums:
        if i == lastNumber:
            newCalledNums.append(i)
            break
        newCalledNums.append(i)
    lastWonBoard = wonBoards.pop()
    print(f"Last board to win: {lastWonBoard} on number {lastNumber}")
    score = sumBoard(lastWonBoard, newCalledNums)
    score = score * lastNumber
    print(score)
    #1284
    return score


if __name__ == '__main__':
    boards, nums = getInput()
    output = part1(boards, nums)
    output = part2(boards, nums)

