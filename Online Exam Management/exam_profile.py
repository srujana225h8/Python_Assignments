import logging

logging.basicConfig(
    filename="exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Exam:
    PLATFORM_NAME = "QSpiders"
    SUBJECT = "Python Programming"
    MARKS_PER_QUESTION = 2
    PASS_MARKS = 40

    def __init__(self, student_name, total_marks):
        if total_marks <= 0:
            logging.error("Invalid total marks for %s | total Marks %s < 0", student_name, total_marks)
            raise ValueError("Total marks must be greater than zero")
        self.student_name = student_name
        self.total_marks = total_marks
        self.marks_obtained = 0
        self.is_started = False
        self.is_submitted = False
        logging.info("Exam profile created for %s", student_name)

    def start_exam(self):
        if self.is_started:
            logging.warning("Exam already started for %s", self.student_name)
            return
        if self.is_submitted:
            logging.warning("Exam already submitted for %s", self.student_name)
            return
        self.is_started = True
        logging.info("Exam started for %s", self.student_name)

    def submit_exam(self, questions_attempted):
        if not self.is_started:
            logging.warning("Submit failed. Exam not started for %s", self.student_name)
            return
        if self.is_submitted:
            logging.warning("Exam already submitted for %s", self.student_name)
            return
        if questions_attempted < 0:
            logging.warning("Zero questions attempted for %s", self.student_name)
            return
        self.is_submitted = True
        self.is_started = False
        self.calculate_score(questions_attempted)
        if self.marks_obtained < self.PASS_MARKS:
            logging.warning("Exam Failed | Marks obtained %s < Pass marks %s", self.marks_obtained, self.PASS_MARKS)
            return
        logging.info(
            "Exam Passed for %s | Marks: %s",
            self.student_name, self.marks_obtained
        )

    def calculate_score(self, questions_attempted):
        if not self.is_submitted:
            logging.warning("Score calculation failed. Exam not submitted for %s", self.student_name)
            return
        if questions_attempted < 0:
            logging.warning("Zero questions attempted for %s", self.student_name)
            return
        self.marks_obtained = self.MARKS_PER_QUESTION * questions_attempted
        if self.marks_obtained > self.total_marks:
            logging.error("Invalid data for attempted questions entered for %s | Marks %s > total marks %s", self.student_name, self.marks_obtained, self.total_marks)
            return
        return self.marks_obtained
        logging.info(
            "Result calculated for %s | Marks: %s ",
            self.student_name, self.marks_obtained
        )

    @classmethod
    def update_pass_marks(cls, new_pass_marks):
        if new_pass_marks <= 0:
            logging.warning("Invalid pass marks entered: %s", new_pass_marks)
            return
        cls.PASS_MARKS = new_pass_marks
        logging.info("Pass marks updated to %s", new_pass_marks)

e1 = Exam("Srujana", 100)
e1.start_exam()
e1.submit_exam(40)
e1.submit_exam(50)
e1.update_pass_marks(50)

e1 = Exam("Swathi", 100)
e1.start_exam()
e1.submit_exam(5)

