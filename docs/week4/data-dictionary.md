# Data Dictionary

The Data Dictionary describes the main data fields used by the Costco Smart Shopping Platform. These fields support product searching, customer accounts, shopping lists, orders, inventory management and personalised shopping features.

| Field Name         | Description                                               | Example Value                           | Required |
| ------------------ | --------------------------------------------------------- | --------------------------------------- | -------- |
| ProductID          | Unique identifier for each product.                       | P1001                                   | Yes      |
| ProductName        | Name of the product displayed to customers.               | Gaming Laptop                           | Yes      |
| ProductDescription | Provides details about the product.                       | 15-inch laptop with 16GB RAM            | Yes      |
| ProductPrice       | Current selling price of the product.                     | 1499.99                                 | Yes      |
| CategoryID         | Identifies the category that the product belongs to.      | C001                                    | Yes      |
| StockQuantity      | Number of units currently available.                      | 25                                      | Yes      |
| CustomerID         | Unique identifier for each customer.                      | CU1001                                  | Yes      |
| CustomerName       | Customer's full name.                                     | John Smith                              | Yes      |
| CustomerEmail      | Email address used for the customer account.              | [john@email.com](mailto:john@email.com) | Yes      |
| CustomerPhone      | Customer contact phone number.                            | 0400123456                              | No       |
| AddressID          | Unique identifier for a customer's delivery address.      | A1001                                   | No       |
| Address            | Customer delivery or billing address.                     | 123 George Street, Sydney NSW           | No       |
| CategoryName       | Name of a product category.                               | Electronics                             | Yes      |
| OrderID            | Unique identifier for each customer order.                | O1001                                   | Yes      |
| OrderDate          | Date and time when an order was created.                  | 2026-10-03                              | Yes      |
| OrderStatus        | Current status of an order.                               | Processing                              | Yes      |
| OrderTotal         | Total value of an order.                                  | 2499.98                                 | Yes      |
| Quantity           | Number of units of a product included in an order.        | 2                                       | Yes      |
| PaymentID          | Unique identifier for a payment transaction.              | PAY1001                                 | Yes      |
| PaymentStatus      | Shows whether the payment was successful or unsuccessful. | Completed                               | Yes      |
| ShoppingListID     | Unique identifier for a customer's shopping list.         | SL1001                                  | No       |
| ReviewID           | Unique identifier for a product review.                   | R1001                                   | No       |
| Rating             | Customer rating given to a product.                       | 5                                       | No       |
| ReviewComment      | Written feedback provided by a customer.                  | Good quality product.                   | No       |

## Data Requirements

The system should use unique identifiers for important entities such as customers, products, orders and payments. Required fields should contain valid information before a record is saved. Optional fields can remain empty when the customer does not provide the information.

