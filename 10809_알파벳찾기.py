al_lst = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']
cnt_lst = [-1]*26
word = input()
idx = 0
for i in range(len(word)):
    for j in range(len(al_lst)):
        if word[i] in word[0:i]:

            break
        if word[i] == al_lst[j]:
            idx = j
            cnt_lst[idx] += i+1
print(*cnt_lst)
