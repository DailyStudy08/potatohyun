'''_런타임 에러...
N, K = map(int, input().split())
mi = N - K
result = 1
while N != 1 or K != 1 or mi != 1:
    result = result*N/(mi*K)
    if N != 1:
        N -= 1
    if K != 1:
        K -= 1
    if mi != 1:
        mi -= 1
print(int(result))
'''
N, K = map(int, input().split())
result = 1
for i in range(1,N+1):
    result *=  i
for j in range(1, K+1):
    result /= j
for k in range(1, N-K+1):
    result /= k
print(int(result))