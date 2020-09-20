def solution(N,K):
    answer = 1
    cnt = 0
    while(N!=1):
        if N % K == 0:
            N = N / K
            cnt += 1
        else:
            N -= 1
            cnt += 1
    answer = cnt

    return answer

# N = 25
# K = 5

N = 578
K = 7

print(solution(N,K))