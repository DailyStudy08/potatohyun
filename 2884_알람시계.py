now_hour = list(map(int,input().split())) #처음 시간, 분
H = now_hour[0] # 알람설정시간 
M = now_hour[1] # 알람설정분

alarm = M - 45 # 당겨진 시간의 분(울려야할 시간)

if alarm >= 0 :
    print(H, alarm)
elif H ==0 and M < 45:
    print(23, alarm+60)
else: 
    print(H-1,alarm+60)
