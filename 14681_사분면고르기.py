quadrant_X = int(input())
quadrant_Y = int(input())

if quadrant_X > 0 :
    if quadrant_Y > 0 :
        print('1')
    else:
        print('4')
        
if quadrant_X < 0 :
    if quadrant_Y > 0 :
        print('2')
    else:
        print('3')