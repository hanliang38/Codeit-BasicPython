# 피타고라스 삼조

for a in range(100 , 333):
    for b in range (200, 500):
        c = 1000 - a - b
        if (a**2 + b**2 == c**2) and ( a < b < c ) and ( a + b + c  == 1000):
            # print( a, b, c )
            print( a * b * c )