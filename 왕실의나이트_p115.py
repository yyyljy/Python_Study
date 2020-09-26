def solution(position):
    answer = 0
    column = position[0]
    row = int(position[1])-1
    colNum = ord(column) - 97
    moveList = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]

    for i in range(len(moveList)):
        if (row + moveList[i][0] >= 0) and (colNum + moveList[i][1] >= 0) and (row + moveList[i][0] < 7) and (colNum + moveList[i][1] < 7):
            answer += 1
    return answer

print(solution('c2'))