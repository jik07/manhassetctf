from flask import Flask, request, render_template
import os
import json

app = Flask(__name__)

with open("db.json", "r") as f:
    db = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", items=db["items"])

@app.route("/item")
def item():
    id = int(request.args.get("id"))
    return render_template("item.html", item=db["items"][id])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)