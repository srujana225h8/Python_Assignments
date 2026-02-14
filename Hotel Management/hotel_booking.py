import logging

logging.basicConfig(
    filename="hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HostelRoom:
    """
    Class representing a Hotel Room
    """

    HOSTEL_NAME = "LAXMI HOTEL"
    ROOM_RENT_PER_MONTH = 5000
    SECURITY_DEPOSIT = 2000

    def __init__(self, student_name, months) -> None:
        """
        Initialize the hotelroom with student name and months
        
        :param student_name: Name of the Student
        :param months: Number of months staying in the Hostel
        """
        if months <= 0:
            logging.error("Invalid months entered for %s | Months %s < 0", student_name, months)
            raise ValueError("Months must be greater than zero")
        self.student_name = student_name
        self.months = months
        self.is_allocated = False
        self.total_fee = 0
        self.deposit_paid = False
        logging.info("Hostel profile created for %s", student_name)

    def calculate_monthly_fee(self):
        """
        Docstring for calculate_monthly_fee
        """
        self.total_fee = (self.months * HostelRoom.ROOM_RENT_PER_MONTH) + HostelRoom.SECURITY_DEPOSIT
        logging.info(
            "Fee calculated for %s | Months: %s | Total Fee: %s",
            self.student_name,
            self.months,
            self.total_fee
        )
        return self.total_fee

    def allocate_room(self, payment):
        if self.is_allocated:
            logging.warning("Room already allocated to %s", self.student_name)
            return
        total = self.calculate_monthly_fee()
        if payment < total:
            logging.error(
                "Insufficient payment for %s | Paid: %s | Required: %s",
                self.student_name,
                payment,
                total
            )
            return
        self.is_allocated = True
        self.deposit_paid = True
        change = payment - total
        logging.info(
            "Room allocated to %s | Paid: %s | Change: %s",
            self.student_name,
            payment,
            change
        )

    def vacate_room(self):
        if not self.is_allocated:
            logging.warning("Vacate failed. Room not allocated to %s", self.student_name)
            return
        refund = HostelRoom.SECURITY_DEPOSIT if self.deposit_paid else 0
        self.is_allocated = False
        self.deposit_paid = False
        self.total_fee = 0
        logging.info(
            "Room vacated by %s | Refund: %s",
            self.student_name,
            refund
        )

    @classmethod
    def update_room_rent(cls, new_rent):
        if new_rent <= 0:
            logging.warning("Invalid room rent entered: %s", new_rent)
            return
        cls.ROOM_RENT_PER_MONTH = new_rent
        logging.info("Room rent updated to %s", new_rent)


h1 = HostelRoom("Srujana", 3)
h1.allocate_room(20000)
h1.vacate_room()
HostelRoom.update_room_rent(6000)
