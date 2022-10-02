'''
stack_1874.스택수열
https://www.acmicpc.net/problem/1874
'''

n = int(input())
lst = list(range(1,n+1))
stack = []
result = []
state = 'keep_going'
for _ in range(n):
    num = int(input())
    if not stack:
        stack.append(lst.pop(0))    # stack이 비어있으면 append하고 시작. 밑에꺼랑 같이하니까 조건너무 덕지덕지...
        result.append('+')
    if stack[-1] <= num:    # num보다 작거나 같으면(같은경우도 그냥 같이 넣어줌)
        while True:
            if stack[-1] == num:
                stack.pop()
                result.append('-')
                break
            else:
                stack.append(lst.pop(0))
                result.append('+')
    elif stack[-1] > num:
        state = 'NO'
        break
if state == 'NO':
    print(state)
else:
    for r in result:
        print(r)

        
'''
문제이해 : 
n이 주어지면 1부터 n까지 숫자가 차례대로 있는 lst가 있다. lst = [1 2 3 4 5 6 7 8 9 10]
입력이 [4 3 6 8 7 5 2 1]라고 볼때
바구니가 있다고 하면 lst에서 4를 꺼내오기 위해 4까지 push해줘야 한다. 그리고 바구니로부터 4를 출력해주기 위해 pop.
그리고 다음 3은 이미 바구니 제일 위에 있으므로 pop.
그리고 6인데, 다시 lst에서 6까지 꺼내려면 5,6을 꺼내니까 push를 두번진행후 pop으로 6을 꺼낸다.
이런식으로 진행한다.
입력2에 보면 입력이 [1 2 5 3 4]인데, 이게 출력이 불가능한 이유는
push, pop으로 1과 2는 넣을 수 있다. 5를 꺼내기 위해 3번의 push후 pop을 해주면 5까지는 꺼내지는데 
이때 바구니의 top은 4이기 때문에 불가능한 연산이라고 볼수있다.
'''
