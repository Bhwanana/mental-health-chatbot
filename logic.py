
from flask import Flask, render_template, request, jsonify
from chatlogic import get_intent, get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("type.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("msg")
    intent = get_intent(user_input)
    reply = get_response(intent)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
