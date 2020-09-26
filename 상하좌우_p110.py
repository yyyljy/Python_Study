def solution(N, schedule):
    answer = '1 1'
    row = 1
    column = 1
    for i in range(0, len(schedule)):
        Move = schedule[i]
        if Move == 'L':
            if column == 1:
                continue
            else:
                column -= 1
        elif Move == 'R':
            if column == int(N):
                continue
            else:
                column += 1
        elif Move == 'U':
            if row == 1:
                continue
            else:
                row -= 1
        else:
            if row < int(N):
                row += 1
    answer = str(row) + ' ' + str(column)
    return answer

N = 5
schedule = ['R','R','R','U','D','D']

print(solution(N,schedule))
