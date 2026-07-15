from flask import Flask, render_template, request

app = Flask(__name__)

# Sample spam keywords
spam_keywords = [
    "win", "winner", "free", "prize", "money",
    "lottery", "click", "offer", "urgent", "claim"
]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        email = request.form["email"].lower()

        if any(word in email for word in spam_keywords):
            prediction = "Spam Email"
        else:
            prediction = "Not Spam"

        return render_template("index.html", prediction=prediction, email=email)

    return render_template("index.html", prediction="", email="")

if __name__ == "__main__":
    app.run(debug=True)