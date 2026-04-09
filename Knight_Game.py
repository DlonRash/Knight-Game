## Board Game Script[D'lon Rash]

# since im gonna want to visualize the project, I'm going to start implementing pygame to help me do so. "Dlon"

import pygame
# screen setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# Drawing Board
cellSize = 80
board = pygame.Surface((cellSize * 8, cellSize * 8))
board_x = (1280 - (cellSize * 8)) // 2
board_y = (720 - (cellSize * 8)) // 2
for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            color = ( (253, 253, 150)) 
        else:
            color = (100, 100, 100)  
        pygame.draw.rect(board, color,  (x * cellSize, y * cellSize, cellSize, cellSize))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Thistle")

    # RENDER YOUR GAME HERE
    screen.blit(board, (board_x, board_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()    
    


import heapq




# this is kara code:

def get_moves(position):
    x,y = position
    
#all possible moves:
    moves_possy = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    valid_moves= []

    for j,k in moves_possy:
        new_x, new_y = x + j, y + k
        
        #keeping the knight within the board:
        if 0 <= new_x <8 and 0 <= new_y <8:
            valid_moves.append((new_x,new_y))
    return valid_moves

#choose your starting position:
x = int(input("Enter an x: "))
if x< 0 or x> 7:
    while x <0 or x >7:
        x = int(input("enter a number between 0 and 7:"))


y = int(input("Enter an y: "))
if 0 > y or y > 7:
       while y <0 or y >7:
        y = int(input("enter a number between 0 and 7:")) 

#choose the target:
tx = int(input("Enter an x for target: "))
if tx< 0 or tx> 7:
    while tx <0 or tx >7:
        tx = int(input("enter a number between 0 and 7:"))

ty = int(input("Enter an y for target: "))
if 0 > ty or ty > 7:
       while ty <0 or ty >7:
        ty = int(input("enter a number between 0 and 7:")) 



startPos = [x,y]
target = [tx, ty]

#creating a tuple here because it keep interfering with the algos
startPos = tuple(startPos)




    # BFS
""" the algorithm will search neighbors, then it childrens, then move the the next level. It used a queue stucture."""

def BFS():
    startPos
    queue = [[startPos]]

    visit_Sq = set()
    visit_Sq.add(startPos)
#while the queue is not empty continue to add it to the path:
    while len(queue) != 0 :
        #FIFO
        path = queue.pop(0)
        #will always be at the last square
        curPos = path[-1]

        if curPos == tuple(target):
            return path
        else:
            for i in get_moves(curPos):
                i = tuple(i)
                if i not in visit_Sq:
                    visit_Sq.add(i)
                    queue.append(path + [i])
        



    #DFS
def DFS():
    """goes all the way down one branch, checks, then backtrack up.(it will repeat these steps)"""

    startPos
    stack = [[startPos]]

    visit_Sq= set()
    visit_Sq.add(startPos)

#while the stack is not empty continue to add it to the path and generate the next movement
    while len(stack) != 0 :
        #FILO and destackings from the back to correctly list(since it last out) the sqaures
        #basically a reverse BFS
        path = stack.pop()
        #will always be at the last square
        curPos = path[-1]

        if curPos == tuple(target):
            return path
        else:
            for i in get_moves(curPos):
                i = tuple(i)
                if i not in visit_Sq:
                    visit_Sq.add(i)
                    stack.append(path + [i])
        

    #A*search
"""determines the shortest base off of heuristics(distance(h)) and dijkstra's(the actucal distance(g))"""

def hur(pos,target):
    #hur can't be negative: this is distance
        new_x = abs(target[0]-pos[0])
        new_y = abs(target[1]-pos[1])

        true_val = new_x+ new_y
    #the knights can only move by 3(in total), so the min is true_value/3

        tru_move = (true_val // 3)
        #can't overestimate h, but also will not serevally underestimate it either
        if true_val % 3 != 0:
                tru_move +=1
        

        return tru_move

def a_search():
#our storage:
    a_list = [] 
    visited = {}  


    # our g, which is the currant cost of the path(I think)
    gCur = 0

#the a*search uses the formula of : f = g(n) + h(n) to find the distance. (Never overshoot the h.)
    f = gCur + hur(startPos, target)

#will push the f and starting position into the top of pq.
    heapq.heappush(a_list, (f, [startPos]))
    visited[startPos] = gCur

    while len(a_list) != 0:
            curSquare, path = heapq.heappop(a_list)
            curPos = path[-1]
            if curPos == tuple(target):
                return path  
            
            for n in get_moves(curPos):
                gNewCur = len(path)  
                fn = gNewCur + hur(n, target)

            # Add to pq only if it cost less
                if n not in visited or gNewCur < visited[n]:
                    visited[n] = gNewCur
                    heapq.heappush(a_list, (fn, path + [n]))


#checking the functions
a = BFS()
print(f"This is BFS: {a}")

b = DFS()
print(f"this is DFS: {b}")

c = a_search()
print(f"This is a*search: {c}")
            