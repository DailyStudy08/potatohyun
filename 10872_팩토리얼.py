'''
stack_10872.팩토리얼
https://www.acmicpc.net/problem/10872
'''

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

N = int(input())
print(factorial(N))