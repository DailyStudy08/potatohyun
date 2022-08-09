now_hour = list(map(int,input().split())) #처음 시간, 분
loading_time = int(input()) # 걸리는 time

end_hour = now_hour[1] + loading_time # 완료후 분
more_hour = end_hour//60    #완료 후 분->시간
if end_hour < 60 and now_hour[0]<24:
    print(now_hour[0],end_hour)
elif end_hour >= 60 and now_hour[0]+more_hour<24:
    print(now_hour[0]+more_hour,end_hour-60*more_hour)
else: #end_hour >= 60 and now_hour[0]+more_hour>=24
    print(now_hour[0]+more_hour-24,end_hour-60*more_hour)
