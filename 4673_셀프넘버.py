def d(n):
    num = n
    for j in range(len(str(n))):
        num += int(str(n)[j])
    return num

arr = []
for i in range(1,10001):
    arr.append(d(i))
nums = set(range(1,10001)) #바로 set으로 생성은 안되나?-가능
selfnumber = sorted(nums-set(arr))
for i in selfnumber:    #리스트로 안바꿔 줘도 for로 뽑기 가능한지-가능
    print(i)