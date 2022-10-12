'''
문자열_5622.다이얼
https://www.acmicpc.net/problem/5622
'''
alphabet = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
word=input()
time=0
for i in range(len(word)):
    for j in alphabet.keys():
        if word[i] in j:
            time+=alphabet[j]
print(time)

'''
1) 알파벳 대문자 리스트를 생성하는 함수
import string
lst = [i for i in string.ascii_uppercase]
print(lst)
2) 알파벳 소문자 리스트를 생성하는 함수
import string
lst = [i for i in string.ascii_lowercase]
print(lst)
3) 대문자+소문자
import string
lst = [i for i in string.ascii_letters]
print(lst)
'''