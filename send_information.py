import stat_server
import logging

class Info(object):
    def send_info(self, stat, param=None): 
    # `stat` is a function definwd in a stat_server module, passed as a str
        stat_func = getattr(stat_server, stat)
        logging.info('logged: {}, {}'.format(stat, param))
        stat_func(param)

