from typing import Counter


dice = list(map(int,input().split()))
s_dice = list(set(dice))
if len(s_dice) == 1 :
    print(10000+s_dice[0]*1000)
elif len(s_dice) == 2:
    result = Counter(dice)
    for k,v in result.items():
        if v >=2:
            print(1000+k*100)
else:
    print(max(dice)*100)