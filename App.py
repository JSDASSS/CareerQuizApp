from flask import Flask, render_template, request
from questions import QUESTIONS, CAREERS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit():
    # Get all the form answers
    answers = request.form.to_dict()
    score = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    # Calculate the score based on user answers
    for question_id, answer in answers.items():
        score[answer] += 1  # Increment the corresponding score for each answer

    # Determine MBTI type from scores
    mbti = (
        ("E" if score["E"] > score["I"] else "I") +
        ("S" if score["S"] > score["N"] else "N") +
        ("T" if score["T"] > score["F"] else "F") +
        ("J" if score["J"] > score["P"] else "P")
    )

    # Get career suggestions based on the MBTI type
    careers = CAREERS.get(mbti, [])

    return render_template('results.html', mbti=mbti, careers=careers)

if __name__ == '__main__':
    app.run(debug=True)
