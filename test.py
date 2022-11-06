while True:
    speak1 = input('이름: ')
    speak2 = input('이름 한개더: ')
    lst = [speak2,speak1]
    if '김동범' in lst :
        if '김연우' in lst:
            print('너넨커플')
        elif '김지현' in lst:
            print('인천사람과 구미사람')
        elif '꼬꼬' in lst :
            print('서울사람과 인천사람')
    elif '김연우' in lst :
        if '김지현' in lst:
            print('불알')
        elif '꼬꼬' in lst :
            print('천생연분')
    elif '김지현' in lst :
        if '꼬꼬' in lst:
            print('우리가 최고')
    else:
        print('똑바로 입력해')
    print('--------------------------------------------')