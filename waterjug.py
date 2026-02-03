from collections import deque

def water_jug(j1,j2,target):
    q= deque([((0,0),[])])
    visited = set()
    
    while q:
        (x,y),path = q.popleft()
        if(x,y) in visited:
            continue;
        visited.add((x,y))
        path=path+[(x,y)]
        
        if x==target or y==target:
            return path
        for nx,ny in [
            (j1,y),(x,j2),#fill
            (0,y),(x,0), #empty
            (x- min(x,j2-y),y+min(x,j2-y)), #1->2
            (x+ min(y,j1-x),y-min(y,j1-x)) #2->1
        ]:
            if(nx,ny) not in visited:
                q.append(((nx,ny),path))
    return None

j1 = int(input("enter the capacity of jug 1: "))
j2 = int(input("enter the capacity of jug 2: "))
target = int(input("enter target amount: "))
solution = water_jug(j1,j2,target)
if(solution):
    print("solution path :")
    for step in solution:
        print(step)
else:
    print("No solution possible")
