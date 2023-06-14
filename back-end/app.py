from flask import Flask, render_template
from flask_cors import CORS
from database import mysqlconnect

app = Flask(__name__)
app.config.from_object(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:8080",
            "allow_headers": "Access-Control-Allow-Origin",
        }
    },
)


@app.route("/")
def helloWorld():
    result = mysqlconnect()
    return render_template("index.html", entries=result)


@app.route("/second", methods=["GET"])
def secondRoute():
    result = mysqlconnect()
    return result


# return "<h1>Hello, World! This is my first Flask Route!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
