from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/new-application")
def new_application():
    return render_template("new-application.html")


if __name__ == '__main__':
    app.run(debug=True)
