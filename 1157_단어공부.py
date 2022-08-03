word = input()
a=list(word.upper())
b=sorted(list(set(word.upper())))
dict = {}
for i in b:
    dict[i] = a.count(i)
max_key1 = max(dict, key = dict.get)
max_value1 = dict[max_key1]
dict[max_key1]=0
# print(max_value1)
max_key2 = max(dict, key = dict.get)
max_value2 = dict[max_key2]
if max_value1 == max_value2:
    print('?')
else:
    for key, value in dict.items():
        if value == 0:
            print(key)

# # # Mississipi
# if len(a) == 1:
#     print(word)
# el