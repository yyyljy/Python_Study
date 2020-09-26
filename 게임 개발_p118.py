def rotate(d):
    if d > 0:
        d -= 1
    else:
        d = 3
    return d

def checkMap(N,M,col,row,d,MAP):
    check = False
    if d == 0:
        #goUP()
        if row > 0:
            if MAP[row-1][col] == 0:
                #goUP
                check = True
    elif d == 1:
        #goRIGHT()
        if col < M - 1:
            if MAP[row][col+1] == 0:
                check = True
    elif d == 2:
        #goDOWN()
        if row < N - 1:
            if MAP[row+1][col] == 0:
                check = True
    elif d == 3:
        #goLEFT()
        if col > 0:
            if MAP[row][col-1] == 0:
                check = True
    return check

def solution(N,M,x,y,d,MAP,answer):
    end = True
    row = y
    col = x
    if MAP[row][col] == 0:
        MAP[row][col] = 2
        answer += 1
    #step1
    direction = d
    d = rotate(d)
    #step2
    while(end):
        #print('row=',row,'col=',col,'d=',d,'direction=',direction)
        #print(MAP)
        if checkMap(N,M,col,row,d,MAP):
            #goUP()
            if d == 0:
                row -= 1        
            #goRIGHT()
            elif d == 1:
                col += 1
            #goDOWN()
            elif d == 2:
                row += 1
            #goLEFT()
            elif d == 3:
                col -= 1
            MAP[row][col] = 2
            answer += 1
            direction = d
        d = rotate(d)
        #step3
        #goBack
        if d == direction:
            #goUP()
            if d == 0:
                if row + 1 < N - 1:
                    row += 1
            #goRIGHT()
            elif d == 1:
                if col > 0:
                    col -= 1
            #goDOWN()
            elif d == 2:
                if row > 0:
                    row -= 1
            #goLEFT()
            elif d == 3:
                if col + 1 < M - 1:
                    col += 1
            if MAP[row][col] == 1:
                end = False
    return answer

N = 4
M = 4
x = 1
y = 1
d = 0
MAP = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
answer = 0
# N = 3
# M = 3
# x = 1
# y = 1
# d = 0
# MAP = [[1,1,1],[1,0,0],[1,1,0]]

print(solution(N,M,x,y,d,MAP,answer))