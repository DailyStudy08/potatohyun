n1, n2 = input().split()

for i in range(2,-1,-1):
    if int(n1[i]) > int(n2[i]):
        print(n1[::-1])
        break
    elif int(n1[i]) < int(n2[i]):
        print(n2[::-1])
        break