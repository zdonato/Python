

##### Edit Distance and Spam (Spell Checker #####
memo = {}
newmemo = {}
hits = 10 
f = open("3esl.txt")
contents = f.read()
words = contents.split("\n")
import time

def fastED(first, second):
    ''' Function returns the edit distacne btwn the strings first and second '''
    if memo.has_key((first,second)):
        return memo[(first,second)]
    elif first == "":
        answer = len(second)
        memo[(first,second)] = answer
        return answer
    elif second == "":
        answer =  len(first)
        memo[(first,second)] = answer
        return answer
    elif first[0] == second[0]:
        answer = fastED(first[1:], second[1:])
        memo[(first,second)] = answer
        return answer
    else:
        substitution = 1 + fastED(first[1:], second[1:])
        deletion = 1 + fastED(first[1:], second)
        insertion = 1 + fastED(first, second[1:])
        answer = min(substitution, deletion, insertion)
        memo[(first,second)] = answer
        return answer
        

def spam():
    ''' Function checks spelling and returns list of close words if spelled incorrectly '''
    print "Type 0 to exit the program." 
    inp = raw_input("spell check> ")
    if inp == "0":
        return
    else: 
        start = time.time()
        if inp in words:
            print 'Correct!' 
        else:
            newl = map(lambda x: [fastED(inp, x),x], words)
            end = time.time()
            elapsed = end - start
            newl.sort()
            print "Suggested Alternatives:"
            def printline(L):
                if L == []:
                    return ""
                else:
                    print "   ",L[0][1]
                    return printline(L[1:])
            print printline(newl[:hits])
            print 'Computation time: ', elapsed
            print " "
            spam()

 
