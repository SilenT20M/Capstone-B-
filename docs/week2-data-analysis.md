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
