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
    




"""Kara's code for our project: """
"""For the abbrivations:
ele = elements
(word)Sq = currant (something)
    aka: curSq = currant Sqaure
"""

def get_moves(position):
    x,y = position
    #all 8 possible moves:
    moves_pos = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    valid_m= []

    for j,k in moves_pos:
        new_x, new_y = x + j, y + k
        
        #keeping the variables in the board:
        if 0 <= new_x <8 and 0 <= new_y <8:
            valid_m.append((new_x,new_y))
    return valid_m


#choose your starting position:
x = int(input("Enter an x: "))
if x< 0 or x> 7:
    while x <0 or x >7:
        x = int(input("enter a number between 0 and 7:"))


y = int(input("Enter an y: "))
if 0 > y or y > 7:
       while y <0 or y >7:
        y = int(input("enter a number between 0 and 7:")) 

#choose the target
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

startPos = tuple(startPos)
target = tuple(target)


#BFS
def BFS():

#seting the lists togethers   
    queue = [[startPos]]
    visitSq = {startPos}

#traveling throughtout the board:
    while len(queue) != 0:
        curPath = queue.pop(0)
        curSq = curPath[-1]
        """print(curSq)"""

        if curSq == target:
            return curPath

        for ele in get_moves(curSq):
            '''print(ele)'''
            #if news positions aren't in the visitSq
            if ele not in visitSq:
                visitSq.add(ele)

                queue.append(curPath+ [ele])

#DFS

"""Just converted the BFS into a DFS by poppin the 1 item"""
def DFS():

#seting the lists togethers   
    queue = [[startPos]]
    visitSq = {startPos}

#traveling throughtout the board:
    while len(queue) != 0:
        curPath = queue.pop()
        curSq = curPath[-1]
        """print(curSq)"""

        if curSq == target:
            return curPath

        for ele in get_moves(curSq):
            '''print(ele)'''
            #if news positions aren't in the visitSq
            if ele not in visitSq:
                visitSq.add(ele)

                queue.append(curPath+ [ele])



def aSearching():
#checking to if target is the currant square
    if startPos == target:
        return [startPos]

   
    seen = {startPos}
    # [score, path]
    q = [[0, [startPos]]]

    while q:
        q.sort() 
#storing the values
        _, path = q.pop(0) 
        
        curr = path[-1]

        for ele in get_moves(curr):
            if ele == target:
                return path + [ele]
            
            if ele not in seen:
                seen.add(ele)
                h = (abs(tx - ele[0]) + abs(ty - ele[1])) / 3
                g = len(path)
                
                q.append([g + h, path + [ele]])
    
        






a = BFS()
print(a)

b = DFS()
print(b)

c = aSearching()
print(c)
            



#tree stuff Chris
class tree:
    def __init__(self, size=8): #cause it's 8*8
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def print_board(self):
        
        print('  ', end='')
        for col in range(1, self.size + 1):
            print(f'{col:2}', end='')
        print()

        
        for row in range(1, self.size + 1):
            print(f'{row} ', end='')
            for col in range(self.size):
                print(f'{self.board[row-1][col]:2}', end='')
            print()
    
    def set_marker(self, row, col, value=' g'):
        if row < 1 or row > 8 or col < 1 or col > 8:
            print("please use numbers between 1 and 8")
            return
        self.board[row-1][col-1] = value

    def set_knight(self, row, col, value=' k'):
        if row < 1 or row > 8 or col < 1 or col > 8:
            print("please use numbers between 1 and 8")
            return
        self.board[row-1][col-1] = value



p = tree()
p.set_marker(tx, ty)   #setting a marker/goal at 4,6
p.set_knight(x, y)    #setting the knight at 5,4
p.print_board()