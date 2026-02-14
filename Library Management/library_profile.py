import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryBook:
    LIBRARY_NAME = "BVRIT Library"
    LOCATION = "Bachupally"
    FINE_PER_DAY = 2

    def __init__(self, book_title, author):
        self.book_title = book_title
        self.author = author
        self.is_issued = False
        self.fine_amount = 0
        logging.info("Book profile created: %s by %s", book_title, author)

    def issue_book(self):
        if self.is_issued:
            logging.warning("Book already issued: %s", self.book_title)
            return
        self.is_issued = True
        logging.info("Book issued: %s", self.book_title)

    def return_book(self, days_late, payment):
        if not self.is_issued:
            logging.warning("Return failed. Book was not issued: %s", self.book_title)
            return
        if days_late < 0:
            logging.error("Invalid late days entered for %s | Dates late %s < 0", self.book_title, days_late)
            return
        if payment < 0:
            logging.error("Invalid payment amount entered for %s | Payment amount %s < 0", self.book_title, payment)
            return
        self.calculate_fine(days_late)
        if payment < self.fine_amount:
            logging.warning("Insufficient payment amount for %s | Payment amount %s < Fine amount %s", self.book_title, payment, self.fine_amount)
            return
        self.is_issued = False
        logging.info(
            "Book returned: %s | Fine payed: %s",
            self.book_title, self.fine_amount
        )

    def calculate_fine(self, days_late):
        if days_late <= 0:
            self.fine_amount = 0
        else:
            self.fine_amount = days_late * LibraryBook.FINE_PER_DAY

        logging.info(
            "Fine calculated for %s | Days Late: %s | Fine: %s",
            self.book_title, days_late, self.fine_amount
        )
        return self.fine_amount

    @classmethod
    def update_fine_per_day(cls, new_fine):
        if new_fine <= 0:
            logging.warning("Invalid fine per day entered: %s", new_fine)
            return
        cls.FINE_PER_DAY = new_fine
        logging.info("Fine per day updated to %s", new_fine)

b1 = LibraryBook("Python", "Guido")
b1.issue_book()
b1.return_book(5,50)
b1.update_fine_per_day(20)
