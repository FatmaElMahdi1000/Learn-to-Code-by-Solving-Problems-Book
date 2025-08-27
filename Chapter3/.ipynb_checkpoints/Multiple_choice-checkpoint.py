def grading(N, Answers, correct_Answers):
    """
    Compare student's answers with the correct answers and return the score.

    Args:
        N (int): Number of questions.
        Answers (list): List of student's answers.
        correct_Answers (list): List of correct answers.

    Returns:
        int: Total number of correct answers if input is valid.
        str: Error message if input is invalid.
    """
    letters = ["A", "B", "C", "D", "E"]
    if not ((len(Answers)) == N) and not (len(correct_Answers) == N):
        return "incorrect number of answers!"
    for answer in Answers:
        if not (answer in letters):
            return "incorrect input!"
    grades = 0
    for i in range(N):
        student_Answer = Answers[i]
        Final_Answer = correct_Answers[i]
        if student_Answer == Final_Answer:
            grades += 1
    return grades
    
N = int(input())
Answers = []
for i in range(1,4):
    answers = input()
    Answers.append(answers)
correct_Answers = []
for j in range(1,4):
    correct_answers = input()
    correct_Answers.append(correct_answers)
    
print(grading(N, Answers, correct_Answers))



    