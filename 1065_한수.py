def num(n):
    global result
    if int(n) < 100:
        result += int(n)
        return result
    else:
        m =int(n)
        if int(n[2])-int(n[1]) == int(n[1])-int(n[0]):
            result += 1
        m -= 1
        return num(str(m))

N = input()
result = 0
print(num(N))