from flask import Flask, render_template, jsonify
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "home.html",
        hostname=socket.gethostname(),
        time=datetime.datetime.now(),
        version=os.getenv("APP_VERSION", "1.0")
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# DevOps health endpoin
@app.route("/health")
def health():
    return jsonify(status="ok")

# Deploy
@app.route("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION", "1.0"),
        hostname=socket.gethostname()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)