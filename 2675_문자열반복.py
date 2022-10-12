# 2
# 3 ABC
# 5 /HTP

# T = int(input())
# for tc in range(T):
#     cnt, word = input().split()
#     for i in word:
#         print(i*(int(cnt)), end='')
#     print()

T = int(input())
for tc in range(T):
    cnt, word = input().split()
    [print(i*(int(cnt)), end='') for i  in word]
