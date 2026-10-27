
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "capstone_b.db"


def insert_sample_data():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    try:
        # Categories
        cursor.executemany("""
            INSERT OR IGNORE INTO Category
            (CategoryID, CategoryName, CategoryDescription)
            VALUES (?, ?, ?)
        """, [
            ("C001", "Electronics", "Electronic devices and accessories"),
            ("C002", "Home and Kitchen", "Products for home and kitchen use"),
        ])

        # Customers
        cursor.executemany("""
            INSERT OR IGNORE INTO Customer
            (CustomerID, CustomerName, CustomerEmail, CustomerPhone)
            VALUES (?, ?, ?, ?)
        """, [
            ("CU1001", "Alex Taylor", "alex@example.com", "0400000001"),
            ("CU1002", "Jordan Lee", "jordan@example.com", "0400000002"),
        ])

        # Customer addresses
        cursor.executemany("""
            INSERT OR IGNORE INTO Address
            (AddressID, CustomerID, Address, Suburb, State, Postcode)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ("A1001", "CU1001", "10 Example Street", "Auburn", "NSW", "2144"),
            ("A1002", "CU1002", "20 Sample Road", "Parramatta", "NSW", "2150"),
        ])

        # Products
        cursor.executemany("""
            INSERT OR IGNORE INTO Product
            (ProductID, ProductName, ProductDescription, ProductPrice,
             CategoryID, StockQuantity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ("P1001", "Wireless Headphones", "Over-ear wireless headphones", 89.99, "C001", 25),
            ("P1002", "Kitchen Blender", "Multi-speed kitchen blender", 59.99, "C002", 15),
        ])

        # Orders
        cursor.executemany("""
            INSERT OR IGNORE INTO CustomerOrder
            (OrderID, CustomerID, OrderDate, OrderStatus, OrderTotal)
            VALUES (?, ?, ?, ?, ?)
        """, [
            ("O1001", "CU1001", "2026-10-10", "Processing", 89.99),
            ("O1002", "CU1002", "2026-10-11", "Completed", 59.99),
        ])

        # Items in each order
        cursor.executemany("""
            INSERT OR IGNORE INTO OrderItem
            (OrderItemID, OrderID, ProductID, Quantity, UnitPrice)
            VALUES (?, ?, ?, ?, ?)
        """, [
            ("OI1001", "O1001", "P1001", 1, 89.99),
            ("OI1002", "O1002", "P1002", 1, 59.99),
        ])

        # Payments
        cursor.executemany("""
            INSERT OR IGNORE INTO Payment
            (PaymentID, OrderID, PaymentDate, PaymentAmount, PaymentStatus, PaymentMethod)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ("PAY1001", "O1001", "2026-10-10", 89.99, "Completed", "Card"),
            ("PAY1002", "O1002", "2026-10-11", 59.99, "Completed", "Card"),
        ])

        # Shopping lists
        cursor.executemany("""
            INSERT OR IGNORE INTO ShoppingList
            (ShoppingListID, CustomerID, ListName, CreatedDate)
            VALUES (?, ?, ?, ?)
        """, [
            ("SL1001", "CU1001", "Weekly Shopping", "2026-10-10"),
            ("SL1002", "CU1002", "Home Essentials", "2026-10-11"),
        ])

        # Products on shopping lists
        cursor.executemany("""
            INSERT OR IGNORE INTO ShoppingListItem
            (ShoppingListItemID, ShoppingListID, ProductID, Quantity)
            VALUES (?, ?, ?, ?)
        """, [
            ("SLI1001", "SL1001", "P1001", 1),
            ("SLI1002", "SL1002", "P1002", 2),
        ])

        # Product reviews
        cursor.executemany("""
            INSERT OR IGNORE INTO Review
            (ReviewID, CustomerID, ProductID, Rating, ReviewComment, ReviewDate)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [
            ("R1001", "CU1001", "P1001", 5, "Good sound quality.", "2026-10-12"),
            ("R1002", "CU1002", "P1002", 4, "Easy to use.", "2026-10-12"),
        ])

        connection.commit()
        print("Sample data inserted successfully!")

        for table in [
            "Category", "Customer", "Address", "Product",
            "CustomerOrder", "OrderItem", "Payment",
            "ShoppingList", "ShoppingListItem", "Review"
        ]:
            count = cursor.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]
            print(f"{table}: {count} records")

    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    insert_sample_data()
