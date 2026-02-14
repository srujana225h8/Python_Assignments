import logging

logging.basicConfig(
    filename="order.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Order:
    PLATFORM_NAME = "Meesho"
    TAX_PERCENTAGE = 5   
    CURRENCY = "INR"

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []   
        self.is_placed = False
        self.is_cancelled = False
        self.total_price = 0
        logging.info("Order profile created for %s", customer_name)

    def place_order(self):
        if self.is_placed:
            logging.warning("Order already placed for %s", self.customer_name)
            return
        if not self.items:
            logging.error("Order cannot be placed. No items added for %s", self.customer_name)
            return
        self.is_placed = True
        logging.info("Order placed successfully for %s", self.customer_name)
        self.items.clear()
        self.total_price = 0


    def add_item(self, item_name, price):
        if price <= 0:
            logging.error("Invalid price for item %s", item_name)
            return
        if self.is_placed:
            logging.warning("Cannot add item. Order already placed for %s", self.customer_name)
            return
        self.items.append((item_name, price))
        logging.info("Item added: %s | Price: %s", item_name, price)

    def calculate_total_price(self):
        if not self.items:
            logging.warning("No items to calculate total for %s", self.customer_name)
            return
        subtotal = 0
        for item in self.items:
            subtotal += item[1]
        tax = (subtotal * Order.TAX_PERCENTAGE) / 100
        self.total_price = subtotal + tax

        logging.info(
            "Total calculated for %s | Subtotal: %s | Tax: %s | Total: %s",
            self.customer_name,
            subtotal,
            tax,
            self.total_price
        )

        return self.total_price

    def cancel_order(self):
        if not self.is_placed:
            logging.warning("Cancel failed. Order not placed for %s", self.customer_name)
            return
        if self.is_cancelled:
            logging.warning("Order already cancelled for %s", self.customer_name)
            return
        self.is_cancelled = True
        logging.info("Order cancelled for %s", self.customer_name)
        self.items.clear()
        self.is_placed = False
        self.total_price = 0


    @classmethod
    def update_tax_percentage(cls, new_tax):
        if new_tax < 0:
            logging.warning("Invalid tax percentage entered: %s", new_tax)
            return

        cls.TAX_PERCENTAGE = new_tax
        logging.info("Tax percentage updated to %s", new_tax)


o1 = Order("Srujana")
o1.add_item("Laptop", 50000)
o1.add_item("Mouse", 1000)
print("Total:", o1.calculate_total_price())
o1.place_order()
o1.cancel_order()
