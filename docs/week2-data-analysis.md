# Capstone B - Week 2 Data Analysis

## Activity 1 & 2: Project Data Inventory

| Data Item | Purpose | Who Creates It? | Who Uses It? | Required? |
| :--- | :--- | :--- | :--- | :--- |
| Product Name | Identifies product | Administrator | Customers | Yes |
| Product SKU | Unique stock identifier | System / Admin | Warehouse, Admin | Yes |
| Product Description | Details feature breakdown | Administrator | Customers | No |
| Product Price | Sales price per unit | Administrator | Customers, Checkout | Yes |
| Stock Level | Tracks inventory quantity | System / Admin | Admin, Cart System | Yes |
| Category ID | Groups related products | Administrator | Search, Navigation | Yes |
| User ID | Unique customer identifier | System | Internal Services | Yes |
| User Email | Login & communications | Customer | System, Admin | Yes |
| Password Hash | Account security credential | Customer / System | Authentication API | Yes |
| User Role | Access permissions | Administrator | Authorization Middleware | Yes |
| Cart Item ID | Identifies items in cart | Customer | Cart Service | Yes |
| Item Quantity | Count of ordered items | Customer | Checkout, Inventory | Yes |
| Order ID | Unique transaction ID | System | Customer, Support | Yes |
| Order Date | Records timestamp | System | Finance, Analytics | Yes |
| Order Status | Tracks delivery lifecycle | System / Admin | Customer, Logistics | Yes |
| Total Amount | Final billed cost | System | Payment Gateway | Yes |
| Shipping Address | Delivery destination | Customer | Logistics API | Yes |
| Payment Status | Tracks transaction completion | Payment Gateway | Order Service, Admin | Yes |
| Tracking Number | Shipment tracking info | Logistics / Admin | Customer, Support | No |
| Revenue Stats | Financial reporting metric | System Aggregator | Management / Admin | Yes |

---
## Activity 3: Data Flow Diagram
```text
┌─────────────────────────────────────────────────────────┐
│                    CUSTOMER / ADMIN                     │
└────────────────────────────┬────────────────────────────┘
                             │ 1. Credentials & Queries
                             ▼
┌─────────────────────────────────────────────────────────┐
│                     USER INTERFACE                      │
└────────────────────────────┬────────────────────────────┘
                             │ 2. Selection & Cart Requests
                             ▼
┌─────────────────────────────────────────────────────────┐
│                   SHOPPING CART SERVICE                 │
│                 └─► [Stock Level Validation]            │
└────────────────────────────┬────────────────────────────┘
                             │ 3. Checkout & Shipping Data
                             ▼
┌─────────────────────────────────────────────────────────┐
│                   ORDER PROCESSING SERVICE              │
│                 ◄─► [Payment Gateway API]               │
└────────────────────────────┬────────────────────────────┘
                             │ 4. Order Records & Logs
                             ▼
┌─────────────────────────────────────────────────────────┐
│                    SECURE DATABASE                      │
└───────────────┬─────────────────────────┬───────────────┘
                │ 5a. Order ID            │ 5b. Metrics
                ▼                         ▼
┌───────────────────────────────┐ ┌───────────────────────┐
│        ORDER TRACKING         │ │    ADMIN DASHBOARD    │
└───────────────────────────────┘ └───────────────────────┘
```
---

## Activity 4: Data Quality and Risk Analysis

| Data Item | Risk | Business Impact | Prevention Strategy |
| :--- | :--- | :--- | :--- |
| **Product Price** | Incorrect or negative value entered | Loss of revenue or customer checkout abandonment | Server-side decimal validation |
| **Password Hash** | Stored in plaintext or weak hashing | Severe security breach and legal liability | Enforce bcrypt/Argon2 hashing |
| **Stock Level** | Race conditions during high traffic | Over-selling products out of stock | Atomic database updates & locking |
| **User Email** | Malformed format or duplicate entry | Failed password resets and account conflicts | Regex check & database `UNIQUE` constraint |
| **Shipping Address**| Missing postcode or street line | Shipping/delivery failure and extra fees | Form validation + Address API lookup |
| **Order Total** | Client-side tampering of total cost | Items sold at reduced or zero cost | Recalculate totals on backend server |
| **User Role** | Unrestricted access permissions | Unauthorized access to admin panel | Role-Based Access Control (RBAC) |
| **Payment Status** | Webhook failure or unsaved status | Orders fulfilled without receiving payment | Retries, logging, & webhook signatures |
| **Product SKU** | Duplicate SKU values assigned | Warehouse & inventory track confusion | Database unique index on SKU column |
| **Tracking Number** | Invalid or incorrectly formatted code | Customers unable to trace shipments | Format validation per carrier spec |

---

## Activity 5: Planning for Future Development

* **Permanent Data:** User accounts, order transaction history, invoice records, and system audit logs.
* **Transient Data:** Active session tokens, guest shopping cart items, and temporary API cache data.
* **Restricted Access:** Admin privileges, financial revenue metrics, database credentials, and customer personal details.
* **Future Reporting Needs:** Monthly sales trends, top-selling categories, user conversion rates, and inventory alerts.
* **Capstone B v2 Expansion:** Support for multi-currency transactions, third-party logistics integrations, and AI product recommendations.

Section 2: Project Data Investigation

| Data Item            | Purpose                          | Creator         | User            | Importance |
| -------------------- | -------------------------------- | --------------- | --------------- | ---------- |
| Product ID           | Uniquely identifies each product | Admin/System    | System          | High       |
| Product Name         | Displays the product name        | Admin           | Customer        | High       |
| Product Description  | Provides product information     | Admin           | Customer        | High       |
| Product Price        | Displays the selling price       | Admin           | Customer/System | High       |
| Product Category     | Groups products for browsing     | Admin           | Customer        | High       |
| Product Image        | Shows the product visually       | Admin           | Customer        | Medium     |
| Stock Quantity       | Shows product availability       | Admin/System    | Customer/Admin  | High       |
| Customer Information | Stores customer details          | Customer        | System/Admin    | High       |
| Shopping Cart Data   | Stores selected products         | Customer/System | Customer        | High       |
| Order Data           | Records completed purchases      | Customer/System | Customer/Admin  | High       |

User Research Participants
| Participant | Role                 | Main Feedback                                                                                                                                                                                   |
| ----------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rahul**   | Team Member / Friend | Wants to find products quickly. Search and filters are important. Product pages should clearly show price, image, description and availability.                                                 |
| **Sujan**   | Team Member / Friend | Checks product details and price before adding something to the cart. Stock availability is important. Wants a simple cart where products can be added, removed or have their quantity changed. |
| **Sandesh** | Team Member / Friend | Wants the shopping website to be simple and easy to use. Product information should be clear, and customer information should be protected.     





| User Gap                        | Research Finding                                                      | Project Requirement                                                          
|

| **Finding products quickly**    | Users do not want to spend too much time looking through products.    | Product search should be included.                                                    |
| **Finding specific products**   | Users need to narrow down products when there are many options.       | Categories, filters and sorting should be available.                                  |
| **Unclear product information** | Users want to know what they are buying before adding it to the cart. | Product name, image, description and price should be clearly displayed.               |
| **Unclear availability**        | Users need to know whether a product is available before purchasing.  | Stock quantity/availability should be shown.                                          |
| **Difficult cart management**   | Users want to easily change quantities or remove products.            | Cart should support add, remove and quantity changes.                                 |
| **Too much complexity**         | Users prefer a simple shopping process.                               | Navigation and main shopping functions should be straightforward.                     |
| **Customer data protection**    | Users expect their personal information to be protected.              | Customer information should have restricted access and appropriate security controls. |


