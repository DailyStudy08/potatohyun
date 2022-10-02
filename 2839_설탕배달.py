def five(n):
    global cnt
    cnt += n // 5
    return (n % 5)
def three(n):
    global cnt
    cnt += n // 3
    return (n % 3)
def re_cal(n):
    global cnt
    if n == 0:
        return
    elif n == 1 or n == 2:
        cnt -= 1
        n += 5
        re_cal(three(n))

N = int(input())
if N == 1 or N == 2 or N == 4 or N == 7:
    print(-1)
else:   
    cnt = 0
    re_cal(three(five(N)))
    print(cnt)
