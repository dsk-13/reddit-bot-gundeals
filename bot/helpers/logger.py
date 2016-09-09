import logging
LOG_PATH = '/var/log/reddit-gundeals-bot.log'
logging.basicConfig(level=logging.INFO, filename=LOG_PATH,
    format='%(asctime)s: %(message)s', datefmt='%b %d %T')
    #format='%(asctime)s: %(message)s', datefmt='%b')
def log(logmessage):
    logging.info(logmessage)
