from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz data
quiz_questions = [
    {"q": "What is the capital of Kenya?", "a": "Nairobi"},
    {"q": "Solve: 5 + 7", "a": "12"},
    {"q": "Who discovered gravity?", "a": "Isaac Newton"}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    feedback = ""
    if request.method == "POST":
        answer = request.form.get("answer", "").strip().lower()
        correct = quiz_questions[0]["a"].lower()
        if answer == correct:
            feedback = "✅ Correct!"
        else:
            feedback = f"❌ Wrong. Correct Answer: {quiz_questions[0]['a']}"
    return render_template("quiz.html", question=quiz_questions[0]["q"], feedback=feedback)

@app.route("/resources")
def resources():
    resources_list = [
        {"title": "Math Revision Notes", "link": "#"},
        {"title": "Science Past Papers", "link": "#"},
        {"title": "Geography Explainer Videos", "link": "#"},
    ]
    return render_template("resources.html", resources=resources_list)

@app.route("/community")
def community():
    return render_template("community.html")

if __name__ == "__main__":
    app.run(debug=True)
