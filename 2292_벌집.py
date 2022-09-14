nums = int(input())
roomnum = 1
result = 1
while nums > roomnum:
    roomnum=roomnum+6*result
    result+=1
print(result)

# while True:
# sum = 1
# stage = 1
# for i in range(1, nums):
#     if sum < nums <= sum + 6*i:
#         stage += 1
#         break
#     else:
#         sum = sum + 6*i
# print(stage)
