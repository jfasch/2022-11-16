import random

num = 0
while num<10:
    num +=1 
    eyes = random.randrange(1,7)
    if eyes == 6:
        print('hurra, nach', num, 'wuerfen')
        break
else:
    print('loser!)
