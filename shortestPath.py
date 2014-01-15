Inf = float("inf")

fiveCities = ["A","B","C","D","E"]

FiveDists = {("A","A"):0, ("A","B"):1, ("A", "C"):3, ("A","D"):7, ("A","E"):Inf,
             ("B", "A"):Inf, ("B","B"):0, ("B","C"):42, ("B","D"):6, ("B","E"):27,
             ("C","A"):Inf, ("C","B"):Inf, ("C","C"):0, ("C","D"):2, ("C","E"):13,
             ("D","A"):Inf, ("D","B"):Inf, ("D","C"):Inf, ("D","D"):0, ("D","E"):5,
             ("E","A"):Inf, ("E","B"):Inf, ("E","C"):Inf, ("E","D"):Inf, ("E","E"):0
             }

def shortestPath(cities,Distances):
    ''' Function takes a list of cities and a dict of distance between them
    and returns the shortest distance '''
    if cities == []:
        return 0
    elif len(cities) == 1:
        return 0
    else:
        one = cities[0]
        two = cities[1]
        useIt = Distances[(one, two)] + shortestPath(cities[1:], Distances)
        loseIt = shortestPath(cities[1:], Distances)
        
    
shortestPath(fiveCities,FiveDists)
