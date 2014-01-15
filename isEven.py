def isEven(l):
    if l == []:
        return []
    elif l[0] % 2 == 0:
        return [l[0]] + isEven(l[1:])
    else:
        return isEven(l[1:])


def iseven(l):
    return filter(lambda x: x% 2 ==0, l) 
