# Business Rules

Business rules define how the data and functions of the Costco Smart Shopping Platform should behave.

### Rule 1 — Customer Accounts

Each customer must have a unique CustomerID.

### Rule 2 — Customer Email

Each customer email address must be unique so that one email cannot be used for multiple customer accounts.

### Rule 3 — Product Identification

Every product must have a unique ProductID.

### Rule 4 — Product Category

Every product must belong to one category.

### Rule 5 — Stock Quantity

Stock quantity cannot be less than zero.

### Rule 6 — Customer Orders

A customer can place multiple orders, but every order must belong to a valid customer.

### Rule 7 — Order Items

Every OrderItem must be connected to both a valid Order and a valid Product.

### Rule 8 — Order Quantity

The quantity of a product in an OrderItem must be greater than zero.

### Rule 9 — Payment

Every completed order must have a valid payment record.

### Rule 10 — Shopping Lists

A customer can create multiple shopping lists, and each shopping list must belong to a valid customer.

### Rule 11 — Shopping List Products

A ShoppingListItem must reference a valid ShoppingList and a valid Product.

### Rule 12 — Product Reviews

A review must be connected to a valid customer and a valid product.

### Rule 13 — Review Rating

Product ratings must use an accepted rating range, such as 1 to 5.

### Rule 14 — Order Status

An order must have a valid status such as Pending, Processing, Completed or Cancelled.

### Rule 15 — Required Information

Required fields must contain valid information before a record can be saved.

## Importance of Business Rules

These rules help maintain accurate and consistent data. They will also guide future database development, backend validation and API behaviour.

