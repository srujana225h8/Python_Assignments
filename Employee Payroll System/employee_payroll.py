import logging

logging.basicConfig(
    filename="payroll.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    COMPANY_NAME = "Qspiders Company"
    HRA_PERCENTAGE = 20    
    LEAVE_DEDUCTION_PER_DAY = 1000

    def __init__(self, emp_name, emp_id, salary):
        if salary <= 0:
            logging.error("Invalid basic salary for %s", emp_name)
            raise ValueError("Basic salary must be greater than zero")
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary
        self.leaves_taken = 0
        self.net_salary = 0
        logging.info("Employee profile created | Name: %s | ID: %s", emp_name, emp_id)

    def apply_leave_deduction(self, leave_days):
        if leave_days < 0:
            logging.warning("Invalid leave days entered for %s", self.emp_name)
            return
        self.leaves_taken = leave_days
        logging.info("Leave recorded for %s | Days: %s", self.emp_name, leave_days)

    def calculate_salary(self):
        hra = (self.salary * Employee.HRA_PERCENTAGE) / 100
        leave_deduction = self.leaves_taken * Employee.LEAVE_DEDUCTION_PER_DAY
        self.net_salary = self.salary + hra - leave_deduction
        if self.net_salary < 0:
            logging.error("Salary calculation error. Negative salary for %s", self.emp_name)
            self.net_salary = 0
        logging.info(
            "Salary calculated for %s | Basic: %s | HRA: %s | Deduction: %s | Net: %s",
            self.emp_name,
            self.salary,
            hra,
            leave_deduction,
            self.net_salary
        )
        return self.net_salary

    def display_payslip(self):
        if self.net_salary == 0:
            logging.warning("Payslip requested before salary calculation for %s", self.emp_name)
            return
        logging.info("---------- PAYSLIP ----------")
        logging.info("Company       : %s", Employee.COMPANY_NAME)
        logging.info("Employee Name : %s", self.emp_name)
        logging.info("Employee ID   : %s", self.emp_id)
        logging.info("Basic Salary  : %s", self.salary)
        logging.info("Leaves Taken  : %s", self.leaves_taken)
        logging.info("Net Salary    : %s", self.net_salary)
        logging.info("-----------------------------")


    @classmethod
    def update_hra_percentage(cls, new_hra):
        if new_hra < 0:
            logging.warning("Invalid HRA percentage entered: %s", new_hra)
            return
        cls.HRA_PERCENTAGE = new_hra
        logging.info("HRA percentage updated to %s", new_hra)

e1 = Employee("Srujana", "EMP101", 50000)
e1.apply_leave_deduction(2)
e1.calculate_salary()
e1.display_payslip()
Employee.update_hra_percentage(25)
