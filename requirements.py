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


class Student:
    def __innit__(
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
