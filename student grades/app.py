from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def calculate_grade(mark):
    if mark >= 90:
        return 'O'
    elif mark >= 80:
        return 'A+'
    elif mark >= 70:
        return 'A'
    elif mark >= 60:
        return 'B+'
    elif mark >= 50:
        return 'B'
    else:
        return 'C'

students = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_name = request.form['student_name']
        roll_number = request.form['roll_number']
        marks = [int(request.form[f'subject{i}']) for i in range(1, 6)]
        grades = [calculate_grade(mark) for mark in marks]
        average_grade = calculate_grade(np.mean(marks))
        student = {
            'student_name': student_name,
            'roll_number': roll_number,
            'marks': marks,
            'grades': grades,
            'average_grade': average_grade
        }
        students.append(student)
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
