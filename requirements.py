from collections import defaultdict


class Student:
    def __init__(
        self, quiz_name, quiz_module, quiz_score, student_id, student_name, sub_date
    ):
        """
        Defines the class of students and expected data.

        Parameters:
        quiz_name (_str_): name of quiz.
        quiz_score(_float_): score of graded quiz.
        quiz_module (_str_): name of module for quiz.
        student_id (_str_): studenty's id number.
        student_name(str_): name of student.
        sub_date(_float): date of submission .

        """
        self.quiz_name = quiz_name
        self.quiz_module = quiz_module
        self.quiz_score = quiz_score
        self.student_id = student_id
        self.student_name = student_name
        self.sub_date = sub_date

    def __repr__(self):
        return f"{self.quiz_name}, {self.quiz_module}, {self.quiz_score}, {self.student_id}, {self.student_name}, {self.sub_date}"


def filter_by_date(date, submissions: list[Student]):
    """
    Provides submissions for a particular date(s).

    Parameters:
        date (_str_): submission date for quiz.
        submissions (list[Student]): List of student's submission infomration.

    Returns:
        sub_list (_list[str]_): a list of corresponding submission dates or empty list.
    """
    sub_list = []
    for submission in submissions:
        if submission.sub_date == date:
            sub_list.append(submission)
    return sub_list


def filter_by_student_id(student_id, submissions: list[Student]):
    """
    Provides submissions for a particular student Id(s).

    Paraneters:
        student_id (_str_): unique set of numbers that represent a student.
        submissions (list[Student]): List of student's submission infomration.

    Returns:
        sub_list (_list[str]_): a list of corresponding submission dates or empty list.
    """
    sub_list = []
    for submission in submissions:
        if submission.student_id == student_id:
            sub_list.append(submission)
    return sub_list


def find_unsubmitted(date, name: list[str], submissions: list[Student]):
    """
    Generates a list of names from a specified list for student(s), with unsubmitted work on a specified date.

    Parameters:
        date (_str_): _date of submissions.
        name (list[str]): _name of student.
        submissions (list[Student]): list of students submissions.

    Returns:
       sub_list (_list[str_]): a list of names of students that have not completed any quiz on that date or empty list.
    """
    sub_list = name
    for submission in submissions:
        if submission.name in name:
            if submission.date == date:
                sub_list.remove(name)
    return sub_list


def get_average_score(quiz_score: list[float]):
    """
    Calculates the average of the list of quiz scores.

    Parameters:
        quiz_score (list[float]): a list of quiz scores.

    Returns:
        _str_: The average of the list of quiz scores presented.
    """
    quiz_average = 0
    for score_of_quiz in quiz_score:
        quiz_average += score_of_quiz
    return f"{quiz_average / len(quiz_score):.1f}"


def get_average_score_by_module(quiz_module: list[Student]):
    """
    Generates a list of modules and the corresponging average of test scores.

    Args:
        quiz_module (list[Student]): a list of the quiz modules used or taken.

    Returns:
        _dict{str,float}_: a dictionary that stores the average score of each module.
    """
    module_dict = defaultdict(list)
    for submission in quiz_module:
        module_dict[submission.quiz_module].append(submission.quiz_score)

    average_by_module = {
        module: float(get_average_score(scores))
        for module, scores in module_dict.items()
    }
    return average_by_module
