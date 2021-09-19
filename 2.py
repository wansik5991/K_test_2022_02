import os
os.system('cls')

# 진수 변환
def convert(num, k) :
    result = ''
    while num > 0 :
        num, mod = divmod(num, k)
        result += str(mod)
    return result[-1::-1]

# 소수 확인
def isPrime(num) :
    if num == 1:
        return 0
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0:
            return 0
    return 1

def solution(n, k):
    print('-'*40)
    n = convert(n,k).split('0')
    answer = 0
    for num in n :
        if num != '' :
            answer += isPrime(int(num))

    return answer

"""print(solution(2, 10))
print(solution(0, 3))
print(solution(4,3))
print(solution(1000000,3))"""
print(solution(999977, 3))
print(solution(437674, 3))
print(solution(110011, 10))