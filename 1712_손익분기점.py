A, B, C = map(int,input().split())
if (B - C) >= 0:
    print(-1)
else:
    print(int(-A/(B - C))+1)
