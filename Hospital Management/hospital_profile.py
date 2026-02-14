import logging

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Patient:
    HOSPITAL_NAME = "AIG Hospital"
    LOCATION = "Kondapur"
    CONSULTATION_FEE = 500

    def __init__(self, name, age, daily_charge):
        self.name = name
        self.age = age
        if daily_charge <= 0:
            logging.error("Invalid daily charge for patient %s | Daily charge: %s < 0", name, daily_charge)
            raise ValueError("Invalid daily charge")
        self.daily_charge = daily_charge
        self.is_admitted = False
        self.bill_amount = 0
        self.is_paid = False
        logging.info("Patient profile created for %s", name)

    def admit(self):
        if self.is_admitted:
            logging.warning("Patient already admitted: %s", self.name)
            return
        self.is_admitted = True
        logging.info("Patient admitted: %s", self.name)

    def discharge(self):
        if not self.is_admitted:
            logging.warning("Discharge failed. Patient not admitted: %s", self.name)
            return
        if not self.is_paid:
            logging.error("Discharge denied. Bill not paid for: %s", self.name)
            return
        self.is_admitted = False
        logging.info("Patient discharged: %s", self.name)

    def calculate_bill(self, days):
        if not self.is_admitted:
            logging.warning("Bill calculation failed. Patient not admitted: %s", self.name)
            return
        if days <= 0:
            logging.warning("Invalid days entered for %s | Days %s < 0", self.name, days)
            return
        self.bill_amount = (
            days * self.daily_charge + Patient.CONSULTATION_FEE
        )
        self.is_paid = False
        logging.info(
            "Bill calculated for %s | Days: %s | Amount: %s",
            self.name, days, self.bill_amount
        )
        return self.bill_amount

    def pay_bill(self, amount):
        if self.bill_amount == 0:
            logging.warning("No bill generated for %s", self.name)
            return
        if amount < self.bill_amount:
            logging.error("Insufficient payment for %s | Amount %s < Bill Amount %s", self.name, amount, self.bill_amount)
            return
        self.is_paid = True
        logging.info("Bill paid for %s | Amount: %s", self.name, amount)

    @classmethod
    def update_consultation_fee(cls, new_fee):
        if new_fee <= 0:
            logging.warning("Invalid consultation fee entered: %s", new_fee)
            return
        cls.CONSULTATION_FEE = new_fee
        logging.info("Consultation fee updated to %s", new_fee)

p1 = Patient("Srujana", 21, 1000)
p1.admit()
p1.calculate_bill(3)
p1.pay_bill(3500)
p1.discharge()
