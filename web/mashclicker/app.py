from flask import Flask, request, render_template
import json

app = Flask(__name__)
FLAG = open("flag.txt").read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/flag", methods=["POST"])
def flag():
    mash = int(request.form.get("mash"))

    if mash >= 999999999999999999999:
        msg = FLAG
    else:
        msg = f"smh not enough mash, need {999999999999999999999-mash} more"

    return {"message": msg}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)