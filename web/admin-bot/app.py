from flask import Flask, request 
from admin_bot import visit_url

app = Flask(__name__)

@app.route("/")
def home():
    response = f"""
    <h1>Cool Text Generator Admin Bot</h1>
    <form action="/submit" method="POST">
            <label for="url">URL to visit:</label>
            <input type="text" name="url" required>
            <br>
            <br>
            <input type="submit" value="Submit to Bot (please don't spam, it takes ~5 seconds)">
    </form>
"""
    
    return response

@app.route("/submit", methods=["POST"])
def login():
    url = request.form["url"]
    
    if visit_url(url):
        return "woah the cooltext u generated is so cool, i suuuuuureeee hope u didnt do anything sneaky"
    else:
        return "grrrr did u rly try to visit a different website >:("

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)