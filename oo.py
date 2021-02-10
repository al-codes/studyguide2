# Create your classes here
class Student():
    """A student class."""

    def __init__(self, first_name, last_name, address):
        """Initialize a student."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

test_student = print(Student('Alex', 'Smith', '1 Hacker Way, Silicon Valley, CA 94306'))


class Question():
    """A question class."""

    def __init__(self, question, answer):
        """Initialize a question."""

        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Prints question and asks user to evaluate it."""
        
        print(self.question)

        usr_answer = input(" >")

        if usr_answer == self.answer:
            return True
        else:
            return False


test_question = print(Question('What is the capital of Alberta?', 'Edmonton'))

#Sample questions & answers for exam
alberta_capital = Question('What is the capital of Alberta?', 'Edmonton')
python_author = Question('Who is the author of Python?', 'Guido Van Rossum')
ubermelon_competitor = Question('www', 'uuu')
balloonicorn_color = Question('bb', 'cc')


class Exam():
    """An exam class."""

    def __init__(self, name):
        """Initializes an exam."""

        self.name = name
        self.questions = []

    def add_question(self, question):
        """Adds question to exam."""

        self.questions.append(question)

    def administer(self):
        """Administers exam and tallies score"""
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1.0

        return score/len(self.questions) * 100


class StudentExam():
    """A student/exam class."""
    score = float()

    def __init__(self, student, exam):
        """Initializes a student and their exam."""

        self.student = student
        self.exam = exam

    def take_test(self):
        """Administers exam and prints score."""

        self.score = self.exam.administer()
        print(f'Your score is {self.score}')

def example():
    """Example student and exam."""

    #Student info taking test
    new_student = Student('Alex', 'Smith', '1 Hacker Way, Silicon Valley, CA 94306')

    #Titling and adding questions to Final exam
    new_exam = Exam('Final Exam')
    new_exam.add_question(alberta_capital)
    new_exam.add_question(python_author)

    #Administer test to Alex
    alex_exam = StudentExam(new_student, new_exam)
    alex_exam.take_test()

#Test run for example exam
example()


class Quiz(Exam):
    """A quiz class."""

    def __init__(self, name):
        """Initializes a quiz - inherits attributes from exam"""
        super().__init__(name)

    def administer(self):
        """Administers quiz and tallies score"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1.0

        if score/len(self.questions) <= 0.5:
            print("Failed")
        else:
            print("Passed")

        return score/len(self.questions) * 100


class StudentQuiz():
    """A student/quiz class."""

    def __init__(self, student, quiz):
        """Initializes a student/quiz"""
        self.score = None
        self.student = student
        self.quiz = quiz 

    
    def take_test(self):
        """Administers quiz and prints pass/fail"""

        self.score = self.quiz.administer()

        #Pass if you do better than 50%
        if self.score > 50.0:
            print("You passed!")
        else:
            print("You failed!")

def example2():
    """Example student and quiz"""

    #Student info taking quiz
    new_student2 = Student('Bob', 'Smith', '1 Hacker Way, Silicon Valley, CA 94306')

    #Titling and adding questions to quiz
    new_quiz = Exam('Pop Quiz')
    new_quiz.add_question(alberta_capital)
    new_quiz.add_question(python_author)
    new_quiz.add_question(ubermelon_competitor)

    #Administer quiz to Bob
    bob_quiz = StudentQuiz(new_student2, new_quiz)
    bob_quiz.take_test()

#Test run for example quiz
example2()