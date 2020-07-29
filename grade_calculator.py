def main():
    """Takes user grade inputs and puts them into grade calculator function"""

    reading_amt = []
    quiz_amt = []
    exam_amt = []
    lab_amt = []
    readings = input("Reading grades: ").split()
    for reading in readings:
        reading = int(reading)
        reading_amt.append(reading)
    reading_total = sum(reading_amt)
    reading_avg = reading_total / len(reading_amt)
    quizzes = input("Quiz grades: ").split()
    for quiz in quizzes:
        quiz = int(quiz)
        quiz_amt.append(quiz)
    quiz_total = sum(quiz_amt)
    quiz_avg = quiz_total / len(quiz_amt)
    exams = input("Exam grades: ").split()
    for exam in exams:
        exam = int(exam)
        exam_amt.append(exam)
    exams_total = sum(exam_amt)
    exam_avg = exams_total / len(exam_amt)
    labs = input("Lab grades: ").split()
    for lab in labs:
        lab = int(lab)
        lab_amt.append(lab)
    lab_total = sum(lab_amt)
    lab_avg = lab_total / len(lab_amt)
    project = int(input("Project grade: "))
    grade_calc(reading_avg, quiz_avg, exam_avg, lab_avg, project)
    gpa_calc(final_average=final_grade)
    letter_calc(final_average=final_grade)


def grade_calc(reading, quiz, exam, lab, project):
    """Calculates average grade using categorical average input from main"""

    global final_grade
    final_grade = (reading * .1) + (quiz * .1) + (exam * .45) + (lab * .25) + (project * .1)
    print(f'Your final grade is: {final_grade:.2f}')


def gpa_calc(final_average):
    """This function computes final grade on a 4.0 scale"""

    gpa = ''
    if final_average >= 90:
        gpa = 4.0
    elif 80 <= final_average <= 89:
        gpa = 3.0
    elif 70 <= final_average <= 79:
        gpa = 2.0
    elif final_average <= 69:
        gpa = 1.0
    else:
        gpa = 0
    print(f'GPA Scale: {gpa}')


def letter_calc(final_average):
    """This function computes final grade on a letter scale"""

    letter = ''
    if final_average >= 90:
        letter = 'A'
    elif 80 <= final_average <= 89:
        letter = 'B'
    elif 70 <= final_average <= 79:
        letter = 'C'
    elif final_average <= 69:
        letter = 'D'
    else:
        letter = 'F'
    print(f'Letter grade: {letter}')


if __name__ == '__main__':
    main()
