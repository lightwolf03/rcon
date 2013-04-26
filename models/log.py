import logging, datetime

def log(*args):
    for arg in args:
        line =  datetime.datetime.strftime(datetime.datetime.now(), "[%d.%m.%Y %H:%M:%S]")
        logging.debug("%s : %s" % (line, arg))