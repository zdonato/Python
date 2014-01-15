memo = {}

def fastLCS(S1, S2):
    ''' Function returns longest common subsequence of two strings '''
    if memo.has_key((S1, S2)):
        return memo[(S1, S2)]
    elif S1 == "" or S2 == "":
        memo[(S1,S2)] = 0
        answer = memo[(S1, S2)] 
        return answer
    elif S1[0] == S2[0]:
        answer = 1 + fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer
        return answer
    else:
        useIt = fastLCS(S1[1:], S2)
        loseIt = fastLCS(S1, S2[1:])
        answer = max(useIt, loseIt)
        memo[(S1, S2)] = answer
        return answer 
