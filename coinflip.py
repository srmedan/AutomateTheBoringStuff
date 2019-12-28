import random
import time


while True:
    time.sleep(2)

    heads = 0
    tails = 0

    for i in range(0, 1001):

        if random.randint(0, 1) == 1:
            heads += 1
        else:
            tails += 1

    print('You now flipped 1000 coins. \n The results are: \n %s heads \n %s tails' %(heads, tails))

