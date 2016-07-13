from flask import Flask, request

app = Flask(__name__)

@app.route("/pixel.js")
def index():
    response = app.make_response('Hello world!')
    #response = app.make_response(
    #        'console.log("Your user agent claims to be {}.");'.format(
    #            request.headers["user-agent"]))
    response.headers['Content-Type'] = 'application/javascript'
    return response

if __name__ == '__main__':
    app.run()
