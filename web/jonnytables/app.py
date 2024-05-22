from flask import Flask, redirect, request, make_response, session
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
flag = open("flag.txt").read()

db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute(f"CREATE TABLE users (username TEXT, password TEXT)")
#db.execute(f"INSERT INTO users VALUES ('bobbytables', '{os.urandom(16).hex()}')")
#db.execute(f"INSERT INTO users VALUES ('rmashburn', 'password123')")
#db.execute(f"INSERT INTO users VALUES ('admin', 'admin')")

@app.route("/")
def home():
    if "username" not in session:
        return redirect("/login")

    response = f"""
    <h1>Welcome, {session["username"]}</h1>
    <p>Here's a funny image (totally unrelated to the challenge, i would never lie mhm mhm)</p>
    <img src="https://imgs.xkcd.com/comics/exploits_of_a_mom.png"/>
"""

    if session["username"] == "jonnytables":
        response += f"<p>{flag}</p>"

    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """
        <h1>Login</h1>
        <form action="/login" method="POST">
            <label for="username">Username:</label>
            <input type="text" name="username" required>
            <br>
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" required>
            <br>
            <br>
            <input type="submit" value="Login">
        </form>
"""

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        query  = db.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'").fetchone()
        if query:
            session["username"] = username
            return redirect("/")
        else:
            return "<p>login failed :P <a href='/login'>try again</a></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)