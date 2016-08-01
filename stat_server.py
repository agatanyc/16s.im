from statsd import StatsClient

statsd  = StatsClient(host = 'localhost',
                      port = 8125,
                      prefix = None,
                      maxudpsize = 512)

def users_stat(param=None):
    statsd.incr('impressions', count=1)

def status_stat(status_code):
    statsd.incr('status_code.{}'.format(status_code), count=1)

def ua_device(device_type):
     statsd.incr('device.{}'.format(device_type), count=1)

def ua_browser(browser):
     statsd.incr('browser.{}'.format(browser), count=1)

def mobile(param=None):
     statsd.incr('device.is_mobile', count=1)

def touch_capable(param=None):
     statsd.incr('device.is_touch_capable', count=1)

def referer(referer):
    statsd.incr('referer.{}'.format(referer), count=1)

def user_id(uuid):
    statsd.incr('user_id.{}'.format(uuid), count=1)

def time_spent(seconds):
    #statsd.incr('time_spent.{}'.format('time_spent'), count=seconds)
    statsd.incr('time_spent', count=seconds)

