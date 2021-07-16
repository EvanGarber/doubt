import time, os

twisted_forms = [['7sBu','2s1u4dBs4d1u','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],['','2s1uJd1u','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],
['','2sLu','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],['','','1u3dHu3d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],['','','','6d3u8s3u6d','3s2d2u2s8d2s2u2d','7sBd'],
['','','1u3dHu3d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],['','2sLu','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],['','2s1uJd1u','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd'],
['7sBu','2s1u4dBs4d1u','1u1d9s1f1t1b9s1d1u','1d1u9s1b1t1f9s1u1d','3s2d2uBs2u2d','7sBd']]

def always_there(sl):
    sw = {'s':' ','u':'_','d':'-','f':'/','b':'\\','t':'|'}
    for i in range(0, len(sl), 2):
        for j in range(int(sl[i],32)):
            print(sw.get(sl[i+1]),end='')
    print()
            
well = int('THEN',32)
# there is a 
def monster():
    # under every bed
    # it acts @night; beware
    for spindly_legs in twisted_forms:
        #wrap from beneath, just out of sight
        #but
        for terror in spindly_legs:
            #it is
            always_there(terror)
        time.sleep(0.1)
        os.system('clear')
# you cannot run from the
monster()
# that you can/t always see
os.system('clear')
for there in twisted_forms[0]:
    # is a form most familiar
    always_there(there)
    # your spindly legs
time.sleep(well)
