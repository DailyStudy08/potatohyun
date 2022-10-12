# 1부터 8까지 차례대로 연주한다면 ascending, 
# 8부터 1까지 차례대로 연주한다면 descending, 
# 둘 다 아니라면 mixed 이다
check = int(input().replace(' ',''))
if check == 12345678:
    print('ascending')
elif check == 87654321:
    print('descending')
else:
    print('mixed')