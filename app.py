from flask import Flask, render_template
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)


@application.route("/")
def index():
    return render_template("index.html")


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/api')

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80)
