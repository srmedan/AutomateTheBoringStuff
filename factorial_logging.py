import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#In case you want it entered to a textfile
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#Uncomment if you want to turn off debugging.
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')