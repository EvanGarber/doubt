import time as wasted, curses, random
console = curses.initscr()
maxdx, maxdy, side, positions, midpoint = 10, 5, range(10000), [], (curses.LINES//2, curses.COLS//2)
curses.curs_set(False)

bounded = 'bounded' #by ambition
n = len(bounded)
for i in range(n):
    positions.append((midpoint[0]-n//2, midpoint[1]-n//2+i, bounded[i]))

def step(positions):
                                                                                 #don't start:
    for i in range(len(positions)):
        step = random.randint(0,3)
        if step == 0 and positions[i][0]+1<=midpoint[0]+maxdy:
            positions[i] = (positions[i][0]+1, positions[i][1], positions[i][2]) #go up,
        elif step == 1 and positions[i][0]-1>=midpoint[0]-maxdy:
            positions[i] = (positions[i][0]-1, positions[i][1], positions[i][2]) #go down,
        elif step == 2 and positions[i][1]+1<=midpoint[1]+maxdx:
            positions[i] = (positions[i][0], positions[i][1]+1, positions[i][2]) #go left,
        elif step == 3 and positions[i][1]-1>=midpoint[1]-maxdx:
            positions[i] = (positions[i][0], positions[i][1]-1, positions[i][2]) #go right,

def expose(positions):
    for pos in positions:
        console.addstr(pos[0],pos[1],pos[2])
    console.refresh()

for ever in side:
    expose(positions) #discover your walls again and again
    wasted.sleep(2/(ever+1)) #you could be doing so much more
    step(positions) #do nothing about it, do all the same
wasted.sleep(1) #you could be doing so much more
curses.endwin()