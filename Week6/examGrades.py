'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 30th, 2023
Version: Python 3.9.6

Exercise 4:
The program checks student answers to an exam quiz against the model answers, and outputs how many correct answers each student achieved.
'''

# Students' answers to exam questions
student_answers = {
    "Adam": ['A', 'B', 'A', 'C', 'C', 'D', 'A', 'D', 'A', 'E'],
    "Bob":  ['D', 'B', 'A', 'B', 'C', 'A', 'C', 'D', 'A', 'E'],
    "Carol":['A', 'C', 'D', 'A', 'C', 'B', 'C', 'D', 'A', 'E'],
    "Jon":  ['C', 'B', 'A', 'E', 'D', 'C', 'A', 'D', 'A', 'E'],
    "Liz":  ['A', 'B', 'A', 'C', 'A', 'E', 'D', 'E', 'A', 'E'],
    "Marc": ['A', 'C', 'D', 'C', 'C', 'D', 'A', 'D', 'A', 'E'],
    "Mia":  ['B', 'B', 'E', 'C', 'A', 'D', 'A', 'D', 'A', 'E'],
    "Zia":  ['E', 'B', 'E', 'C', 'A', 'E', 'C', 'E', 'A', 'E']
}

# Key to the questions
model_answers = ['A', 'C', 'D', 'C', 'A', 'D', 'A', 'D', 'A', 'E']

# Grade all answers
for name in student_answers:
    # Grade for one student
    correctCount = 0
    for j in range(len(student_answers[name])):
        if student_answers[name][j] == model_answers[j]:
            correctCount += 1
    print(name, "achieved", correctCount, "correct answers.")

# Returning a dictionary containing the grade achieved per person
grades = {}
def get_grades():

    for name in student_answers:
        # Grade for one student
        correctCount = 0
        for j in range(len(student_answers[name])):
            if student_answers[name][j] == model_answers[j]:
                correctCount += 1
        grades[name] = correctCount
    print(grades)

# Displaying students in ascending order
def sorted_by_grade():
    print(sorted(grades.items(), key = lambda x:x[1]))

# Calling functions
def main():
    get_grades()
    sorted_by_grade()

main()