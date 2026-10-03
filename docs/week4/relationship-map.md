# Relationship Map

The relationship map explains how the main entities in the Costco Smart Shopping Platform are connected.

## Customer → Address

A customer can have one or more addresses.

* One Customer can have many Addresses.
* Each Address belongs to one Customer.

Relationship:

**Customer 1 → Many Address**

---

## Customer → Order

A customer can place multiple orders.

* One Customer can place many Orders.
* Each Order belongs to one Customer.

Relationship:

**Customer 1 → Many Order**

---

## Category → Product

Products are organised into categories.

* One Category can contain many Products.
* Each Product belongs to one Category.

Relationship:

**Category 1 → Many Product**

---

## Order → OrderItem

An order can contain multiple products.

* One Order can contain many OrderItems.
* Each OrderItem belongs to one Order.

Relationship:

**Order 1 → Many OrderItem**

---

## Product → OrderItem

A product can appear in many order items.

* One Product can appear in many OrderItems.
* Each OrderItem refers to one Product.

Relationship:

**Product 1 → Many OrderItem**

---

## Order → Payment

An order is associated with payment information.

* One Order can have a Payment record.
* Each Payment belongs to one Order.

Relationship:

**Order 1 → 1 Payment**

---

## Customer → ShoppingList

Customers can create shopping lists.

* One Customer can have many ShoppingLists.
* Each ShoppingList belongs to one Customer.

Relationship:

**Customer 1 → Many ShoppingList**

---

## ShoppingList → ShoppingListItem

A shopping list can contain multiple items.

* One ShoppingList can contain many ShoppingListItems.
* Each ShoppingListItem belongs to one ShoppingList.

Relationship:

**ShoppingList 1 → Many ShoppingListItem**

---

## Product → ShoppingListItem

Products can be added to many shopping lists.

* One Product can appear in many ShoppingListItems.
* Each ShoppingListItem refers to one Product.

Relationship:

**Product 1 → Many ShoppingListItem**

---

## Customer → Review

Customers can provide product reviews.

* One Customer can create many Reviews.
* Each Review belongs to one Customer.

Relationship:

**Customer 1 → Many Review**

---

## Product → Review

Products can receive multiple reviews.

* One Product can have many Reviews.
* Each Review refers to one Product.

Relationship:

**Product 1 → Many Review**

---

## Overall Relationship Structure

The database connects customers with their addresses, orders, shopping lists and reviews. Products are connected to categories, orders through OrderItems, shopping lists through ShoppingListItems and customers through reviews. Payments are connected to orders.

These relationships help reduce duplicated data and provide a clear structure for the future database.

