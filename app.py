from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return f"Hello {socket.gethostname()}"



if __name__ == "__main__":
    print("Hi")
    app.run(host="0.0.0.0", port="80")