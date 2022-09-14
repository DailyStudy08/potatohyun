# N, M = map(int,input().split())
# poketmon = []
# for _ in range(N):
#     poketmon.append(input())

# for _ in range(M):
#     find = input()
#     if find.isdigit():
#         print(type(find))
#         print(poketmon[int(find)-1])
#     else:
#         if find in poketmon:
#             print(poketmon.index(find)+1)


###########타임에러->딕셔너리로 풀어야하는 문제##############3
N, M = map(int,input().split())
poketmon = {}
for i in range(1,N+1):
    poketmon[i] = input()

for _ in range(M):
    find = input()
    if find.isdigit():
        print(poketmon[int(find)]) 
    else:
        for k, v in poketmon.items(): 
            if v == find:
                print(k)

