import logging

# ordrr of logging

# second stage
# logging.basicConfig(level = logging.INFO)

# Third stage
# logging.basicConfig(level = logging.DEBUG)

# Fourth stage
# logging.basicConfig(level = logging.DEBUG, filename='log.txt', filemode = 'a')

# sixth stage

logging.basicConfig(level = logging.DEBUG, filename='log.txt', filemode = 'a', format="%(asctime)s - %(levelname)s -%(message)s")

# NOTE: these lines of codes had to initially and if you run one  more time it will give you error
logging.debug(" This is the lowest priority error")# Lowest priority
logging.info(" This is  the info error")
logging.warning("This is  the waning error")
logging.error("This is an error message")

# #seventh stage
# name = 'ramu'
# logging.debug(f'The boys name is {name}')

#Eigth stage
# try: 
#     1/0
# except ZeroDivisionError as e:
#     logging.error("ZeroDivisionError", exc_info=True)
    
#ninth satge
try: 
    1/0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")

    

