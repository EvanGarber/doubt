import curses; from time import sleep as and_you; from random import randint as ri
console = curses.initscr()
curses.curs_set(False)

my_attention = 'may I have your attention, please'
attention = my_attention.split(' ')

t, hopes = [(curses.LINES//2,curses.COLS//2-len(my_attention)//2,my_attention)], range(len(my_attention))
truth, life, cant_die, dont_live = range(1500), 100, 0.1, 0.02
def superficially():
    console.refresh()
def live():
    global t
    for i, ph in enumerate(t):
        console.addch(ph[0],ph[1],ph[2][0])
        t[i] = (ph[0],ph[1]+1,ph[2][1:])
    t = [p for p in t if len(p[2])>0]
def we_rebound():
    s = ri(0,len(attention)-1)
    e = ri(s+1,len(attention))
    wl = attention[s:e]
    for i in range(len(wl)):
        if ri(0,1):
            wl[i] = wl[i].upper()
    ph = ' '.join(wl)
    x = ri(0,curses.COLS-len(ph)-1)
    y = ri(0,curses.LINES-1)
    t.append((y,x,ph))

for this in hopes:
    live()
    superficially()
    and_you(cant_die)
for this in truth:
    live()
    superficially()
    and_you(dont_live)
    for all in range(this//life):
        we_rebound()
# you can always see the mess in retrospect
and_you(4) # must
# remember to remember it
curses.endwin()