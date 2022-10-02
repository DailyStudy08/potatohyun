X = int(input())
N = int(input())
sum = 0
for _ in range(N) :
    price, cnt = map(int,input().split())
    sum += price*cnt
if sum == X:
    print('Yes')
else:
    print('No')