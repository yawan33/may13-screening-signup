from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("participants")
        with open("data.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, number])
        return render_template("success.html")
    return render_template("form.html")

if __name__ == "__main__":
    app.run()
