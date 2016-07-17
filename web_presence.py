"""Service to collect analytics for a given website.
"""
from flask import Flask, request
from user_agents import parse
from urlparse import urlparse
import uuid
import datetime
import statsd
import stat_server


app = Flask(__name__)

@app.route('/pixel.js')
def index():
    # Create response object
    response = app.make_response(
            'console.log("Your user agent claims to be {}.");'.format(
                request.headers['user-agent']))
    response.headers['Content-Type'] = 'application/javascript'

    # create cookie to be set on a given browser
    UUID = bytes(uuid.uuid4())
    print UUID , 'XXXXXXXXXXX'
    now = datetime.datetime.now()
    future = now + datetime.timedelta(days=90)
    # cookie will expire in 90 days
    response.set_cookie('user_id', value=UUID, expires=future)

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
        referer = referer_parsed.netlock.split(':')[0]
        stat_server.referer(referer)

    stat_server.status_stat(response.status_code)

    return response
    
#__________________________

def log_status_code(res):
    stat_server.status_stat(res.status_code)
    return res

@app.route('/page/<id>')
def display_message(id):
    stat_server.users_stat()
    return 'Page ID is {} !'.format(id)

app.after_request(log_status_code) # the parameter function will run 
                                   # after each request

if __name__ == '__main__':
    app.debug = True
    app.run()

