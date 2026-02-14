import logging

logging.basicConfig(
    filename="movie.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MovieTicket:
    THEATRE_NAME = "PVR Cinemas"
    TICKET_PRICE = 200
    TAX_PERCENTAGE = 5

    def __init__(self, customer_name, number_of_tickets):
        if number_of_tickets <= 0:
            logging.error("Invalid ticket count for %s | Number of Tickets: %s < 0", customer_name, number_of_tickets)
            raise ValueError("Number of tickets must be greater than zero")
        self.customer_name = customer_name
        self.number_of_tickets = number_of_tickets
        self.is_booked = False
        self.is_cancelled = False
        self.total_amount = 0
        logging.info("Movie ticket profile created for %s", customer_name)

    def calculate_ticket_price(self):
        base_amount = self.number_of_tickets * MovieTicket.TICKET_PRICE
        tax = (base_amount * MovieTicket.TAX_PERCENTAGE) / 100
        self.total_amount = base_amount + tax
        logging.info(
            "Ticket price calculated for %s | Tickets: %s | Base: %s | Tax: %s | Total: %s",
            self.customer_name,
            self.number_of_tickets,
            base_amount,
            tax,
            self.total_amount
        )
        return self.total_amount

    def book_seat(self, payment):
        if self.is_booked:
            logging.warning("Seats already booked for %s", self.customer_name)
            return
        total = self.calculate_ticket_price()
        if payment < total:
            logging.error(
                "Insufficient payment for %s | Paid: %s | Required: %s",
                self.customer_name,
                payment,
                total
            )
            return
        self.is_booked = True
        change = payment - total
        logging.info(
            "Seats booked for %s | Paid: %s | Change: %s",
            self.customer_name,
            payment,
            change
        )

    def cancel_booking(self):
        if not self.is_booked:
            logging.warning("Cancellation failed. No booking found for %s", self.customer_name)
            return
        if self.is_cancelled:
            logging.warning("Booking already cancelled for %s", self.customer_name)
            return
        self.is_cancelled = True
        self.is_booked = False
        self.total_amount = 0
        logging.info(
            "Booking cancelled for %s",
            self.customer_name,
        )

    @classmethod
    def update_ticket_price(cls, new_price):
        if new_price <= 0:
            logging.warning("Invalid ticket price entered: %s", new_price)
            return
        cls.TICKET_PRICE = new_price
        logging.info("Ticket price updated to %s", new_price)

m1 = MovieTicket("Srujana", 3)
m1.book_seat(1000)
m1.cancel_booking()
MovieTicket.update_ticket_price(250)
