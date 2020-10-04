def solution(s):
    answer = len(s)
    for i in range(int(len(s)/2),0,-1):
        tmp = len(s)
        word = s[0:i]
        cnt = 1
        j = i
        while j < len(s):
            if word == s[j:j+i]:
                cnt += 1
                if cnt == 2:
                    tmp -= i-1
                elif cnt > 2:
                    tmp -= i
                    if cnt == 10:
                        tmp += 1
                    if cnt == 100:
                        tmp += 1
                    if cnt == 1000:
                        tmp += 1
                j += i
                continue
            else:
                cnt = 1
                word = s[j:j+i]
                j += i
        answer = min(answer,tmp)
    return answer

s= 'a'
print(solution(s))
# # #a
# # #1
s = 'aabbaccc'
print(solution(s))
# # #2a2ba3c
# # #7
s = 'abcabcdede'
print(solution(s))
# # #2abcdede
# # #8
s = 'ababcdcdababcdcd'
print(solution(s))
# # #2ababcdcd
# # #9
s = 'abcabcabcabcdededededede'
print(solution(s))
#14
#2abcabc2dedede

