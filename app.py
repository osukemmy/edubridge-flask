from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)

# Database connection
db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT 'Hello from MariaDB!'")
    result = cursor.fetchone()
    return render_template("home.html", message=result[0])

# New deck route
@app.route("/deck")
def deck():
    return render_template("deck.html")

# Run the Flask app locally
if __name__ == "__main__":
    app.run(debug=True)

