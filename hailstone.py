def hailstone_sequence(a_0):
    l=[]
    while a_0 != 1:
        l.append(a_0)
        if a_0 % 2 == 0:
            a_0 /= 2
        else:
            a_0 = 3*a_0+1
    l.append(1)
    return l
