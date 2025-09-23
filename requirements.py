# "quizName": "string",
# "quizModule": "string",
# "quizScore": number,
# "studentId": number,
# "studentName": "string",
# "submissionDate": "string"
# Filter By Date Feature (filter_by_date)
# 1. Given I have a list of submission objects, when I call the filterByDate function with
# a date and the list of submissions (in that order), then a list of submission objects
# with a submissionDate equal to that date are returned to me, so I can see all
# submissions for a particular date.
# 2. Given I have supplied a date and a list of submission objects (in that order), when
# the list is empty, or the filter by date feature does not find any results, then I am
# returned an empty list.

from collections import defaultdict


class Student:
    def __init__(
        self, quiz_name, quiz_module, quiz_score, student_id, student_name, sub_date
    ):
        self.quiz_name = quiz_name
        self.quiz_module = quiz_module
        self.quiz_score = quiz_score
        self.student_id = student_id
        self.student_name = student_name
        self.sub_date = sub_date


def filter_by_date(date, submissions: list[Student]):
    sub_list = []
    for submission in submissions:
        if submission.sub_date == date:
            sub_list.append(submission)
    return sub_list


# Filter By StudentId Feature (filter_by_student_id)
# 1. Given I have a list of submission objects, when I supply a studentId and the list (in
# that order) to the filter_by_student_id function, then submission objects with a
# studentId equal to the studentId I supplied are returned to me, so I can see all
# submissions for a particular student.
# 2. Given I have supplied a studentId and a list of submission objects (in that order),
# when the list is empty, or the filter_by_student_id feature does not find any results,
# then I am returned an empty list.


def filter_by_student_id(student_id, submissions: list[Student]):
    sub_list = []
    for submission in submissions:
        if submission.student_id == student_id:
            sub_list.append(submission)
    return sub_list


# Find Unsubmitted Feature (find_unsubmitted)
# 1. Given I have a list of submission objects, when I supply a date, a list of student
# names, and a list of submission objects (in that order) to the find_unsubmitted
# function, then I am returned a list of names of students that have not completed
# any quiz on that date.
# 2. Given that the find unsubmitted feature does not find any student names, I am
# returned an empty list.


def find_unsubmitted(date, name: list[str], submissions: list[Student]):
    sub_list = name
    for submission in submissions:
        if submission.name in name:
            if submission.date == date:
                sub_list.remove(name)
    return sub_list


# Get Quiz Average Feature (get_average_score)
# 1. Given I have a list of submission objects, when I supply that list to the
# get_average_score function, I am returned an average of all the quiz scores.
# 2. Given that I have received an average of the quiz scores, it has a precision of one
# decimal place (example: 76.6).


def get_average_score(quiz_score: list[float]):
    quiz_average = 0
    for score_of_quiz in quiz_score:
        quiz_average += score_of_quiz
    return f"{quiz_average / len(quiz_score):.1f}"


# Quiz Average by Module Feature (get_average_score_by_module)
# 1. Given I have a list of submission objects, when I supply that list to the
# get_average_score_by_module function, I am returned an object.
# 2. Given that I have received an object from this feature, then there is one key for
# every unique module name in the submission list, and the keys are the module
# names.
# 3. Given that I have a list of submission objects from only one module, when I use the
# quiz average by module feature, then the resulting object contains only one key.
# 4. When I have received an object from this feature, the value of each key should be
# the average of quiz scores from that module.
# Example:
# {
# "Statistics": 83.5,
# "Algebra": 79.6,
# "History": 80.1
# }


def get_average_score_by_module(quiz_module: list[Student]):
    module_dict = defaultdict(list)
    for submission in quiz_module:
        module_dict[submission.quiz_module].append(submission.quiz_score)
    
    average_by_module = {
    module: float(get_average_score(scores))
    for module, scores in module_dict.items()
}
    return average_by_module
    
    
# addresss{ key =var: val = functions}
    
    
    # print(module_dict)


#     if module_name not in module_scores:
#     module_scores[module_name] = []
# module_scores[module_name].append(score)
Submission_list = [
    Student("Quiz 1", "Math", 85.0, "S001", "Alice", "2025-09-20"),
    Student("Quiz 1", "Math", 90.0, "S002", "Bob", "2025-09-20"),
    Student("Quiz 1", "Math", 78.0, "S003", "Charlie", "2025-09-20"),
    Student("Quiz 1", "Math", 92.0, "S004", "David", "2025-09-21"),
    Student("Quiz 1", "Math", 88.0, "S005", "Eve", "2025-09-21"),
    Student("Quiz 2", "Science", 80.0, "S001", "Alice", "2025-09-22"),
    Student("Quiz 2", "Science", 70.0, "S002", "Bob", "2025-09-22"),
    Student("Quiz 2", "Science", 75.0, "S003", "Charlie", "2025-09-22"),
]

get_average_score_by_module(Submission_list)