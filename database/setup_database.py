
import sqlite3
from pathlib import Path

# Save the database in this folder.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "capstone_b.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    tables = [
        """
        CREATE TABLE IF NOT EXISTS Category (
            CategoryID TEXT PRIMARY KEY,
            CategoryName TEXT NOT NULL,
            CategoryDescription TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID TEXT PRIMARY KEY,
            CustomerName TEXT NOT NULL,
            CustomerEmail TEXT NOT NULL UNIQUE,
            CustomerPhone TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Address (
            AddressID TEXT PRIMARY KEY,
            CustomerID TEXT NOT NULL,
            Address TEXT NOT NULL,
            Suburb TEXT,
            State TEXT,
            Postcode TEXT,
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Product (
            ProductID TEXT PRIMARY KEY,
            ProductName TEXT NOT NULL,
            ProductDescription TEXT NOT NULL,
            ProductPrice REAL NOT NULL CHECK (ProductPrice >= 0),
            CategoryID TEXT NOT NULL,
            StockQuantity INTEGER NOT NULL CHECK (StockQuantity >= 0),
            FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS CustomerOrder (
            OrderID TEXT PRIMARY KEY,
            CustomerID TEXT NOT NULL,
            OrderDate TEXT NOT NULL,
            OrderStatus TEXT NOT NULL,
            OrderTotal REAL NOT NULL CHECK (OrderTotal >= 0),
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS OrderItem (
            OrderItemID TEXT PRIMARY KEY,
            OrderID TEXT NOT NULL,
            ProductID TEXT NOT NULL,
            Quantity INTEGER NOT NULL CHECK (Quantity > 0),
            UnitPrice REAL NOT NULL CHECK (UnitPrice >= 0),
            FOREIGN KEY (OrderID) REFERENCES CustomerOrder(OrderID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Payment (
            PaymentID TEXT PRIMARY KEY,
            OrderID TEXT NOT NULL UNIQUE,
            PaymentDate TEXT,
            PaymentAmount REAL NOT NULL CHECK (PaymentAmount >= 0),
            PaymentStatus TEXT NOT NULL,
            PaymentMethod TEXT,
            FOREIGN KEY (OrderID) REFERENCES CustomerOrder(OrderID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ShoppingList (
            ShoppingListID TEXT PRIMARY KEY,
            CustomerID TEXT NOT NULL,
            ListName TEXT NOT NULL,
            CreatedDate TEXT NOT NULL,
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ShoppingListItem (
            ShoppingListItemID TEXT PRIMARY KEY,
            ShoppingListID TEXT NOT NULL,
            ProductID TEXT NOT NULL,
            Quantity INTEGER NOT NULL CHECK (Quantity > 0),
            FOREIGN KEY (ShoppingListID)
                REFERENCES ShoppingList(ShoppingListID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Review (
            ReviewID TEXT PRIMARY KEY,
            CustomerID TEXT NOT NULL,
            ProductID TEXT NOT NULL,
            Rating INTEGER NOT NULL CHECK (Rating BETWEEN 1 AND 5),
            ReviewComment TEXT,
            ReviewDate TEXT NOT NULL,
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
            UNIQUE (CustomerID, ProductID)
        )
        """
    ]

    try:
        for table_sql in tables:
            cursor.execute(table_sql)

        connection.commit()
        print("Database created successfully!")
        print(f"Database location: {DB_PATH}")
        print("Created 10 tables:")
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name
        """)
        for (table_name,) in cursor.fetchall():
            print(f"- {table_name}")

    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
