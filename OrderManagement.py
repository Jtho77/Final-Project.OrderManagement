# Importing necessary modules
from breezypythongui import EasyFrame

class OrderManager(EasyFrame):
    """Main application class for the Efficient Order Manager."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Efficient Order Manager")

        # Add the components
        self.addLabel(text="Order ID:", row=0, column=0)
        self.orderIDField = self.addIntegerField(value=0, row=0, column=1)

        self.addLabel(text="Customer Name:", row=1, column=0)
        self.customerNameField = self.addTextField(text="", row=1, column=1)

        self.addLabel(text="Product:", row=2, column=0)
        self.productField = self.addTextField(text="", row=2, column=1)

        self.addLabel(text="Quantity:", row=3, column=0)
        self.quantityField = self.addIntegerField(value=1, row=3, column=1)

        self.addButton(text="Add Order", row=4, column=0, columnspan=2, command=self.addOrder)

        self.orderListBox = self.addListbox(row=5, column=0, columnspan=2)
        self.addButton(text="View Orders", row=6, column=0, columnspan=2, command=self.viewOrders)

        self.orders = []

    def addOrder(self):
        """Handles adding a new order."""
        order = {
            "orderID": self.orderIDField.getNumber(),
            "customerName": self.customerNameField.getText(),
            "product": self.productField.getText(),
            "quantity": self.quantityField.getNumber()
        }
        self.orders.append(order)
        self.messageBox(title="Success", message="Order added successfully!")

    def viewOrders(self):
        """Displays the list of orders."""
        self.orderListBox.clear()
        for order in self.orders:
            self.orderListBox.insert(END, f"Order ID: {order['orderID']}, Customer: {order['customerName']}, Product: {order['product']}, Quantity: {order['quantity']}")

# Run the program
if __name__ == "__main__":
    OrderManager().mainloop()
