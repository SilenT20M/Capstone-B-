# Design Notes

## Overview

During Week 4, our team organised the information collected during Weeks 2 and 3 into a database design package. The purpose of this documentation is to provide a clear blueprint for the future Costco Smart Shopping Platform.

## Entity Decisions

We created the Customer entity because the system needs to store customer account and contact information.

The Product entity was created to store information about products available through the shopping platform.

The Category entity was created because products need to be organised into categories. This can make product searching and browsing easier.

The Order and OrderItem entities were separated because one order can contain multiple products. Separating them also reduces duplicated information.

The Payment entity was created to store payment information connected to customer orders.

ShoppingList and ShoppingListItem were created to support the shopping list functionality identified during our project investigation.

The Review entity was created to allow customers to provide feedback and ratings about products.

## Relationship Decisions

We connected Customer to Order because customers can place multiple orders.

We connected Category to Product because products are organised into categories.

We connected Order to OrderItem because an order can contain multiple products.

We connected Product to OrderItem because the same product can appear in different customer orders.

We connected Customer to ShoppingList because customers can create and manage their own shopping lists.

We connected Product to ShoppingListItem because products can be added to shopping lists.

We connected Customer and Product to Review because customers provide reviews for specific products.

## Business Rule Decisions

Business rules were included to make sure the database contains valid and consistent information.

For example, product stock cannot be negative, customer emails should be unique, and order quantities must be greater than zero.

These rules can later be implemented through database constraints and backend validation.

## Challenges

One challenge during the design process was deciding which information should be stored as separate entities. We needed to avoid storing the same information in multiple places.

Another challenge was identifying the correct relationships between products, orders and customers. The team reviewed the project requirements and previous investigation work before finalising the relationships.

## Data Normalisation

The design separates related information into different entities to reduce unnecessary duplication.

For example, product information is stored in Product instead of being repeated for every order. OrderItem connects the product with a specific order and stores the quantity and purchase price.

## Future Improvements

Future versions of the system could include:

* Supplier information
* Store location information
* Product promotions and discounts
* Inventory alerts
* Product recommendations
* Delivery tracking
* Customer loyalty information
* More detailed reporting and analytics
* Integration with real-time Costco inventory systems

## Team Review

The Week 4 documentation should be reviewed by all team members before the final submission. Each member should contribute at least one meaningful update or review to the repository.

The documentation will provide a shared reference for the team when backend development and database implementation begin.

