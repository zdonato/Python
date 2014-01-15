def fib(n):
    ''' Returns the nth fibonacci term ''' 
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fib(n-1) + fib(n-2)

def fibByThirds(n):
    ''' Returns the (x*3)th fib number '''
    l = n *3
    return fib(l)



