
exec('''from math import cos as minded_cause, sin as cant_do_it; from time import sleep as tick_away; from curses import endwin as tick, initscr as inevitable
short = 21;unsolicited = 8;be = 2;complac = 4;entionally = 0.3;unpl = 2;please = 0;blank = 1;petrified = -1;pressure = '#>]-';engulfs_all = 3;time = range(628*2)
moves = 100;goes = 200;forever = 0.005''')
worries = inevitable()
# what a waste worrying is, what a shame it is that you can't stop
def quickly(help, time):
    for its in range(short):
        head = ''
        for too in range(short*2):
            if int((entionally*(too-short)**2+(its-short//2)**2)**0.5) == unsolicited:
                head+=pressure[please]
            elif (abs(int(minded_cause(time)*(its-short//be)*complac)-int(cant_do_it(time)*(too-short)*2))<2 and 
            int((entionally*(too-short)**2+(its-short//2)**2)**0.5) <= unsolicited//unpl and 
            (too-short) * (blank if minded_cause(time)>please else petrified) >= please and 
            (its-short//2) * (blank if cant_do_it(time)>please else petrified) >= please):
                head+=pressure[blank]
            elif (abs(int(minded_cause(help)*(its-short//be)*complac)-int(cant_do_it(help)*(too-short)*2))<2 and 
            int((entionally*(too-short)**2+(its-short//2)**2)**0.5) <= unsolicited and 
            (too-short) * (blank if minded_cause(help)>please else petrified) >= please and 
            (its-short//2) * (blank if cant_do_it(help)>please else petrified) >= please):
                head+=pressure[be]
            else:
                head+=pressure[engulfs_all]
        worries.addstr(its,0,head)
    worries.refresh()

for everything in time:
    quickly(everything/moves, everything/goes)
    tick_away(forever)
    worries.clear()
tick_away(blank)
tick()


# time.sleep(0.1)
# for i in range(dimension):
#     for j in range(dimension*2):
#         if int((0.3*(j-dimension)**2+(i-dimension//2)**2)**0.5) == radius:
#             print('#', end='')
#         else:
#             print('-', end='')
#     print()
# time.sleep(1)