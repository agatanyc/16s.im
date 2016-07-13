from flask import Flask, request

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route("/")
    def index():
        response = app.make_response('Hello world!')
        #response = app.make_response(
        #        'console.log("Your user agent claims to be {}.");'.format(
        #            request.headers["user-agent"]))
        response.headers['Content-Type'] = 'application/javascript'
        return response

    app.run()
