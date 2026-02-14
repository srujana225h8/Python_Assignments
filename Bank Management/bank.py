import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BankAccount:
    BANK = "SBI"
    IFSC = "SBI0001"
    COUNTRY = "India"
    MINIMUM_BALANCE = 1000

    def __init__(self, name, phone, balance, age):
        if balance < BankAccount.MINIMUM_BALANCE:
            logging.error(
                "Account creation failed for %s | Balance %s < Minimum Balance %s",
                name, balance, BankAccount.MINIMUM_BALANCE
            )
            raise ValueError("Insufficient opening balance")
        if age <= 0:
            logging.error("Invalid age for %s", name)
            raise ValueError("Invalid age")
        self.name = name
        self.phone = phone
        self.balance = balance
        self.age = age
        logging.info("Account created for %s | Balance: %s", name, balance)

    def withdraw(self, amount):
        if amount <= 0:
            logging.warning("Invalid withdrawal amount for %s: %s", self.name, amount)
            return
        if self.balance - amount < BankAccount.MINIMUM_BALANCE:
            logging.error(
                "Withdrawal denied for %s | Min balance violation | Balance: %s",
                self.name,
                self.balance
            )
            return
        self.balance -= amount
        logging.info(
            "Withdrawn %s from %s | Remaining Balance: %s",
            amount,
            self.name,
            self.balance
        )

    def deposit(self, amount):
        if amount <= 0:
            logging.warning("Invalid deposit amount for %s: %s", self.name, amount)
            return
        self.balance += amount
        logging.info(
            "Deposited %s to %s | Updated Balance: %s",
            amount,
            self.name,
            self.balance
        )

    def display_details(self):
        logging.info("Bank     : %s", BankAccount.BANK)
        logging.info("IFSC     : %s", BankAccount.IFSC)
        logging.info("Country  : %s", BankAccount.COUNTRY)
        logging.info("Name     : %s", self.name)
        logging.info("Age      : %s", self.age)
        logging.info("Phone    : %s", self.phone)
        logging.info("Balance  : %s", self.balance)

    @classmethod
    def update_minimum_balance(cls, new_minimum_balance):
        if new_minimum_balance <= 0:
            logging.warning("Invalid minimum balance entered: %s", new_minimum_balance)
            return
        cls.MINIMUM_BALANCE = new_minimum_balance
        logging.info("Minimum balance updated to %s", new_minimum_balance)


c1 = BankAccount("Srujana", 9866756345, 10000, 21)
c1.display_details()
c1.withdraw(5000)
c1.withdraw(-100)
c1.withdraw(0)
c1.withdraw(4500)
c1.withdraw(10000)

c1.deposit(-10)
c1.deposit(5000)

BankAccount.update_minimum_balance(2000)
c1.withdraw(8000)

c1.display_details()
