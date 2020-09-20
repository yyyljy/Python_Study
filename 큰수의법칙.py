#배열의 크기 N
#더해지는 횟수 M
#연속가능 K
import time
def solution(N,M,K,Arr):
    answer = 0

    # 리스트에서 가장 큰 수 pop
    maxnum1 = Arr.pop(Arr.index(max(Arr)))
    # 리스트에서 두 번째로 큰 수 pop
    maxnum2 = Arr.pop(Arr.index(max(Arr)))
    
    # 몇 바퀴
    cycle = int(M / (K+1))
    remainder = M % cycle
    
    # 계산
    answer = maxnum1 * (K * cycle + remainder) + (maxnum2 * cycle)


    #print('maxnum1=',maxnum1)
    #print('maxnum2=',maxnum2)
    
    #print('cycle=',cycle)
    #print(cycle+(M%cycle))

    # print(cycle)
    # print(3*cycle+(M%cycle))
    # print(maxnum1 * (3*cycle+(M%cycle)))
    # print((maxnum2 * cycle))

    return answer

N = 5
M = 10000
K = 3
Arr = [2,4,5,4,6]

# N = 5
# M = 7
# K = 1
# Arr = [3,4,3,4,3]

start = time.time()
print(solution(N,M,K,Arr))
end = time.time()
print(end-start)