x, y, w, h = map(int, input().split())
min_lst = [x,y,(w-x), (h-y)]

print(min(min_lst))

