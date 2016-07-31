"""Service to collect analytics for a given website.
"""
from flask import Flask, request, render_template
from user_agents import parse
from urlparse import urlparse
from collections import defaultdict
import uuid
import datetime
import statsd
import stat_server


app = Flask(__name__)

@app.route('/index')
def index():
    # Create response object
    response = app.make_response(render_template('index.html', time_spent=0))
    response.headers['Content-Type'] = 'text/html'
    print request.args.get('leaving', 'no value!!!')
    if request.args.get('leaving', ''):
        time_spent = request.args.get('timeSpent', '0')
        stat_server.time_spent(int(time_spent))

    # create cookie to be set on a given browser
    UUID = bytes(uuid.uuid4())
    print UUID , 'XXXXXXXXXXX'
    now = datetime.datetime.now()
    future = now + datetime.timedelta(days=90)
    # cookie will expire in 90 days
    response.set_cookie('user_id', value=UUID, expires=future)
    stat_server.user_id(UUID)

    # parse `user_agent` from the responce headers
    ua_string = request.headers['user-agent']
    user_agent = parse(ua_string)

    device_type = user_agent.device.family
    stat_server.ua_device(device_type)

    browser = user_agent.browser.family
    stat_server.ua_browser(browser)

    is_mobile = user_agent.is_mobile
    if is_mobile:
        stat_server.mobile()

    is_touch_capable = user_agent.is_touch_capable
    if is_touch_capable:
        stat_server.touch_capable()

    if request.headers.get('referer'):
        referer_parsed =  urlparse(request.headers['referer'])
        referer = referer_parsed.netloc.split(':')[0]
        stat_server.referer(referer)

    stat_server.status_stat(response.status_code)

    stat_server.users_stat()


    return response
    
if __name__ == '__main__':
    app.debug = True
    app.run()

