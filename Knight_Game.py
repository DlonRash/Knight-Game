## Board Game Script[D'lon Rash]

# since im gonna want to visualize the project, I'm going to start implementing pygame to help me do so. "Dlon"

import pygame
# screen setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.display.set_caption("Knight Path Visualization")
running = True

font = pygame.font.SysFont(None, 28)
Knight_Piece = pygame.image.load(R"c:\Users\5310\Documents\GitHub\Knight-Game\Knight free icons designed by Victoruler.png")
Knight_Piece = pygame.transform.scale(Knight_Piece, (80, 80))

# Drawing Board/Setting up board
cellSize = 80
board = pygame.Surface((cellSize * 8, cellSize * 8))
board_x = (1280 - (cellSize * 8)) // 2
board_y = (720 - (cellSize * 8)) // 2

for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            color = (255, 253, 208)
        else:
            color = (150, 75, 0)
        pygame.draw.rect(board, color, (x * cellSize, y * cellSize, cellSize, cellSize))


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
    
        
# Board Game Script (Cont'd)

# compute paths
bfs_path = BFS()
dfs_path = DFS()
aSearching_path = aSearching()

# gonna try and visualize each state
mode = "BFS"
index = 0
timer = pygame.time.get_ticks()
delay = 300 # ms per state
def get_current_path_and_color(mode):
    if mode == "BFS":
        return bfs_path, (0,200,0)
    elif mode == "DFS":
        return dfs_path, (200,0,0)
    elif mode == "aSearching":
        return aSearching_path, (0,0,200)
    else:
        return [], (0,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((225,217,209))

    # RENDER YOUR GAME HERE
    
    screen.blit(board, (board_x, board_y))
    # current knight position
    if index > 0 and path:
        Knight_square = path[min(index - 1, len(path)-1)]
    else:
        Knight_square = startPos
    
    kx = board_x + Knight_square[0] * cellSize
    ky = board_y + Knight_square[1] * cellSize
    screen.blit(Knight_Piece, (kx, ky))
    now = pygame.time.get_ticks()
    


    path, color = get_current_path_and_color(mode)
    # Start square being drawn
    start_px = board_x + target[0] * cellSize
    start_py = board_y + target[1] * cellSize
    pygame.draw.rect(screen, (255, 255, 0), (start_px, start_py, cellSize, cellSize), 4)

    # Target square being drawn
    target_px = board_x + target[0] * cellSize
    target_py = board_y + target[1] * cellSize
    pygame.draw.rect(screen, (0, 0, 0), (target_px, target_py, cellSize, cellSize), 4)
    # draw path leading to current index
    for i in range(index):
        if i < len(path):
            px = board_x + path[i][0] * cellSize
            py = board_y + path[i][1] * cellSize
            pygame.draw.rect(screen, color, (px, py, cellSize, cellSize), 4)



    # drawing the path
    for i in range(index):
        x,y = path[i]
        px = board_x + x * cellSize
        py = board_y + y * cellSize
        pygame.draw.rect(screen, color, (px, py, cellSize, cellSize))
    # advancing each step of the path
    if now - timer> delay and index<len(path):
        index += 1
        timer = now
    # switchin to next algroithim
    if index>= len(path) and mode != "DONE":
        pygame.time.wait(800)
        if mode == "BFS":
            mode = "DFS"
        elif mode == "DFS":
            mode = "aSearching"
        else:
            mode = "DONE"
        index = 0
        timer = pygame.time.get_ticks()
       
       
    label = font.render(f"Mode: {mode}", True, (0,0,0))
    screen.blit(label, (20,20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()    
        

                