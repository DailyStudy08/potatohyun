# def function(num):
#     cnt = 0
#     if num == 1:
#         return cnt
#     elif num % 3 == 0 :
#         num = num / 3
#         cnt += 1
#     elif num % 2 == 0 :
#         num = num / 2
#         cnt += 1
#     else:
#         num -= 1
#         cnt += 1


# num = int(input())
# cnt = 0
# print(cnt,num)
# while num != 1:
#     if num % 3 == 0 :
#         num = num / 3
#         cnt += 1
#         print(cnt,num)
#     elif (num - 1) % 3 == 0:
#         num -= 1
#         cnt += 1
#         print(cnt,num)
#     elif num % 2 == 0 :
#         num = num / 2
#         cnt += 1
#         print(cnt,num)
#     else:
#         num -= 1
#         cnt += 1
#         print(cnt,num)
# print(cnt)


n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])