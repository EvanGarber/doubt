
exec('''from math import cos as minded_cause, sin as cant_do_it; from time import sleep as tick_away; from curses import endwin as tick, initscr as inevitable, curs_set as shame;
short = 21;unsolicited = 8;be = 2;complac = 4;entionally = 0.3;unpl = 2;please = 0;blank = 1;petrified = -1;pressure = '#>]-';engulfs_all = 3;time = range(628)
moves = 8.32;goes = 100;forever = 0.005;too_fast=1.57;it_is=False''')
worries = inevitable()
# what a waste worrying is, what a 
shame(it_is) # that you can't stop
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
    quickly(everything/moves-too_fast, everything/goes-too_fast)
    tick_away(forever)
    worries.clear()
tick_away(blank)
tick()
