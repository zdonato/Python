def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

memo = {}

def fastFib(n):
    ''' Nth Fibonacci number, assuming N is a non-negative integer. '''
    if memo.has_key(n):
        answer = memo[n]
        return answer
    elif n == 0:
        memo[n] = 0
        answer = memo[n] 
        return answer
    elif n == 1:
        memo[n] = 1
        answer = memo[n]
        return answer
    else:
        memo[n] = fastFib(n-1) + fastFib(n-2)
        answer = memo[n]
        return answer
