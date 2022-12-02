from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/new-application")
def new_application():
    return render_template("new-application.html")


@app.route("/view-applications")
def view_application():
    return render_template("view-application.html")


@app.route("/application-details")
def application_details():
    return render_template("application-details.html")


if __name__ == '__main__':
    app.run(debug=True)
