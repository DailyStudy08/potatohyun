'''
기초수학_2869.달팽이는 올라가고 싶다.
https://www.acmicpc.net/problem/2869
'''
A, B, V = map(int, input().split())     # A : 낮에 올라감, B : 밤에 떨어짐, V : 나무높이

# sum = 0
# day = 0
# if A - B == 1:
#     day = V - B
# else:
#     while True:
#         day += 1
#         sum += A
#         if sum >= V:
#             break
#         sum -= B
# print(day)

'''
처음엔 런타임 에러나서
if A - B == 1:
    day = V - B
이걸 넣어주니까 시간초과.

'''
# day = 0
# if A - B == 1:
#     day = V - B
# else:
#     day += 1
#     dis = A - B     #하루가 지난뒤 이동한 거리(올라간거리-미끄러진거리) 
#     V = V - A
#     while V > 0:
#         day += 1
#         V -= dis
#         if V <= 0 :
#             break
# print(day)

'''
또 런타임 에러
'''
day = 0
if V - A <= 0:
    day = 1
# if A - B == 1:
#     day = V - B
else:
    # print('걸림')
    day += 1
    # print('확인용 day1=',day)
    dis = A - B     #하루가 지난뒤 이동한 거리(올라간거리-미끄러진거리) 
    # print(V,A,B)
    V = V - A
    # print(dis,V)
    if V % dis == 0:
        day += V // dis
    else:
        day += V // dis + 1
    # print('확인용 day2=',day)

print(day)
'''
또또
'''
'''
보통 런타임에러가 발생하는 이유는 다음과 같다.
1. 배열의 범위가 너무 적거나 많을 때
2. 0으로 무언가를 나눴을 때
3. 메모리를 과다하게 사용했을 떄
'''

A, B, V = map(int, input().split()) 

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else:
    print((V-B) // (A-B)+1)

'''
결국 런타임에러 고치지 못하고 구글링.
근데 클틀에서는 비슷한 흐름으로 접근했는데
끝에 조금 다름
'''