C = int(input())
for _ in range(C):
    N, *score = map(int,input().split())
    sum = 0
    for i in score:
        sum += i
    aver = sum/N
    cnt = 0
    for j in score:
        if j > aver:
            cnt += 1
    top_st = cnt/N*100
    # 소수 n번째 자릿수까지 반올림
    # round(실수,n)
    # 소수점아닌 정수 반올림은 n을 -값으로 설정.
    # print(f'{round(top_st,3)} %')

    # tc1의 경우 40.0으로 나오는데 우리는 40.000을 받아야 한다.
    # 이때는 format을 써주면 된다.
    print("{:.3f}%".format(top_st))