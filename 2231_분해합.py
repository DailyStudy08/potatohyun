# def bs(n):
#     lst = []
#     # nnum = 0
    
#     for i in range(1,n+1):
#         sum = 0
#         nn = i
#         for _ in range(len(str(i))):
#             sum += nn % 10
#             nn = nn//10
#         lst.append(i + sum)
#         if (i + sum) == n:
#             return i



N = int(input())
lst = []
for i in range(1,N+1):
    sum = 0
    nn = i
    for _ in range(len(str(i))):
        sum += nn % 10
        nn = nn//10
    lst.append(i + sum)
    if (i + sum) == N:
        print(i)
        break
if N not in lst:
    print(0)

