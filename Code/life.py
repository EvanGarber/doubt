import random, time

def life(your_life):
    for days in your_life:
        you_can = int('LIVE',32)/(days+1)
        try:
            #to not fall apart
            #make goals
            print('succeed and fail')
        except:
            #we
            pass
            #away eventually, try
        while you_can>0:
            print(' '*(int(you_can)//10) + 'until you can\'t')
            you_can -= int('DIE',32)
        time.sleep(0.5/(days+1))

days_per_year = 365
years = random.uniform(0,100)
your_life = range(0, int(days_per_year*years))
life(your_life)
