N, M = map(int, input().split())
no_li = set()
no_lo = set()
for _ in range(N):
    no_li.add(input())
for _ in range(M):
    no_lo.add(input())
unknown = list(no_li & no_lo)
# list()랑 [] 는 다르다!
# list()는 형변환 할수있고 []는 안됨.


unknown.sort()
# set은 sort가 안도고 set은 append가 아니라 add를 사용
print(len(unknown))
for name in unknown:
    print(name)

#####

# for _ in range(N+M):
#     a = input()
#     if a in no_li:
#         unknown.append(a)
#     else:
#         no_li.append(a)
# unknown.sort()
# print(len(unknown))
# for name in unknown:
#     print(name)
    