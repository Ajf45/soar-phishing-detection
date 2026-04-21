from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("reports/incident.json") as f:
        data = json.load(f)

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)