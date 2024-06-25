from flask import Flask, render_template
import time
import tkinter as tk

app = Flask(__name__)

@app.route("/")
def start():

    return render_template("index.html", background_image='Photos/time.jpg')
@app.route("/blog/")
def blog():

    return render_template("blog.html", background_image='Photos/88.jpg')
@app.route("/contacts/")
def contacts():

    return render_template("contacts.html",background_image='Photos/99.jpg')
@app.route("/time/")
def time():
    return render_template('time.html', background_image='Photos/time.jpg')

if __name__ == "__main__":
    app.run()