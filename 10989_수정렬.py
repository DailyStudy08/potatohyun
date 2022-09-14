# N = int(input())
# lst = []
# for _ in range(N):
#     lst.append(input())
# lst.sort()
# for i in lst:
#     print(i)

# N = int(input())
# lst = ''
# for _ in range(N):
#     lst += (' '+input())
# tmp = list(map(int,lst.split()))
# for _ in range(N):
#     print(min(tmp))
#     tmp.remove(min(tmp))

'''
문제 이상^^
import sys

N = int(sys.stdin.readline())
lst = [0] * 10001
for n in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)

'''