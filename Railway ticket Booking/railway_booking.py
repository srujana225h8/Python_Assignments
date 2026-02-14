import logging

logging.basicConfig(
    filename="ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:
    RAILWAY_NAME = "Indian Railways"
    BASE_FARE = 100
    TAX_PERCENTAGE = 5

    def __init__(self, passenger_name, distance_km):
        if distance_km <= 0:
            logging.error("Invalid distance for %s", passenger_name)
            raise ValueError("Distance must be greater than zero")
        self.passenger_name = passenger_name
        self.distance_km = distance_km
        self.is_booked = False
        self.is_cancelled = False
        self.total_fare = 0
        logging.info("Ticket profile created for %s", passenger_name)

    def book_ticket(self, payment):
        if self.is_booked:
            logging.warning("Ticket already booked for %s", self.passenger_name)
            return
        total = self.calculate_fare()
        if payment < total:
            logging.error(
                "Insufficient payment for %s | Paid: %s | Required: %s",
                self.passenger_name,
                payment,
                total
            )
            return
        self.is_booked = True
        change = payment - total
        logging.info(
            "Ticket booked for %s | Fare: %s | Paid: %s | Change: %s",
            self.passenger_name,
            total,
            payment,
            change
        )


    def cancel_ticket(self):
        if not self.is_booked:
            logging.warning("Cancellation failed. Ticket not booked for %s", self.passenger_name)
            return
        if self.is_cancelled:
            logging.warning("Ticket already cancelled for %s", self.passenger_name)
            return
        self.is_cancelled = True
        logging.info("Ticket cancelled for %s. No refund available.", self.passenger_name)

    def calculate_fare(self):
        basic_fare = self.distance_km * Ticket.BASE_FARE
        tax = (basic_fare * Ticket.TAX_PERCENTAGE) / 100
        self.total_fare = basic_fare + tax
        logging.info(
            "Fare calculated for %s | Distance: %s | Basic: %s | Tax: %s | Total: %s",
            self.passenger_name,
            self.distance_km,
            basic_fare,
            tax,
            self.total_fare
        )
        return self.total_fare

    @classmethod
    def update_base_fare(cls, new_base_fare):
        if new_base_fare <= 0:
            logging.warning("Invalid base fare entered: %s", new_base_fare)
            return
        cls.BASE_FARE = new_base_fare
        logging.info("Base fare updated to %s", new_base_fare)


t1 = Ticket("Srujana", 10)
t1.book_ticket(500)
t1.cancel_ticket()
Ticket.update_base_fare(120)
t2 = Ticket("Akshara", 45)
t2.book_ticket(20)
t2.cancel_ticket()

