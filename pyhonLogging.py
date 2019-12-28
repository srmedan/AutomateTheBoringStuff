""" Python logging setting (basic) """

#uncomment if you want to turn off debugging
#logging.disable(logging.CRITICAL)

"""
# Log Levels

debug
info
warning
error
critical

"""

#In case you want it entered to a textfile
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')