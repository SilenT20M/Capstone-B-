# Entity List

The following entities represent the main objects required by the Costco Smart Shopping Platform. These entities can be used as the main tables when the database is developed.

## 1. Customer

Fields:

* CustomerID
* CustomerName
* CustomerEmail
* CustomerPhone

Purpose:

Stores customer account and contact information.

## 2. Address

Fields:

* AddressID
* CustomerID
* Address
* Suburb
* State
* Postcode

Purpose:

Stores customer delivery and billing address information.

## 3. Product

Fields:

* ProductID
* ProductName
* ProductDescription
* ProductPrice
* CategoryID
* StockQuantity

Purpose:

Stores information about products available through the shopping platform.

## 4. Category

Fields:

* CategoryID
* CategoryName
* CategoryDescription

Purpose:

Groups products into categories to make product searching and browsing easier.

## 5. Order

Fields:

* OrderID
* CustomerID
* OrderDate
* OrderStatus
* OrderTotal

Purpose:

Stores information about customer orders.

## 6. OrderItem

Fields:

* OrderItemID
* OrderID
* ProductID
* Quantity
* UnitPrice

Purpose:

Stores the individual products included in an order.

## 7. Payment

Fields:

* PaymentID
* OrderID
* PaymentDate
* PaymentAmount
* PaymentStatus
* PaymentMethod

Purpose:

Stores payment information associated with an order.

## 8. ShoppingList

Fields:

* ShoppingListID
* CustomerID
* ListName
* CreatedDate

Purpose:

Stores customer shopping lists for products they want to purchase or remember.

## 9. ShoppingListItem

Fields:

* ShoppingListItemID
* ShoppingListID
* ProductID
* Quantity

Purpose:

Connects products to a customer's shopping list.

## 10. Review

Fields:

* ReviewID
* CustomerID
* ProductID
* Rating
* ReviewComment
* ReviewDate

Purpose:

Stores customer feedback and ratings for products.

## Entity Summary

The main entities are Customer, Address, Product, Category, Order, OrderItem, Payment, ShoppingList, ShoppingListItem and Review. These entities cover the main shopping, product, customer and transaction requirements identified during the project investigation.

