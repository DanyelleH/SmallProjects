create database consumers;
\connect consumers

DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    id serial PRIMARY KEY,
    first_name varchar(100),
    last_name varchar(150),
    email_address varchar(150) UNIQUE,
    dob DATE,
    address varchar(255)
);

INSERT INTO Customers(first_name,last_name,email_address,dob,address) VALUES
    ('daniel', 'johnson', 'dj@gmail.com', '08-09-1995', '123 Some Street Overthere, Somewhere 98765'),
    ('susan', 'smith', 'susan.smith@gmail.com', '03-04-1990', '456 Elm St, Somecity, 12345'),
    ('michael', 'brown', 'mike.brown@gmail.com', '11-15-1987', '789 Pine Rd, Othertown, 67890'),
    ('emily', 'davis', 'emily.davis@aol.com', '06-22-1992', '101 Oak Ave, Anytown, 23456'),
    ('john', 'wilson', 'john.wilson@ehotmail.com', '12-30-1985', '202 Birch Blvd, Everywhere, 34567'),
    ('olivia', 'martinez', 'olivia.martinez@hotmail.com', '01-19-2003', '303 Maple Ln, Village, 45678'),
    ('jacob', 'garcia', 'jacob.garcia@gmail.com', '07-25-1991', '404 Cedar St, Townville, 56789'),
    ('maria', 'hernandez', 'maria.hernandez@ymail.com', '09-10-2006', '505 Redwood Dr, Suburbia, 67891'),
    ('liam', 'moore', 'liam.moore@ymail.com', '02-13-1989', '606 Sequoia Way, Metropolis, 78901');

CREATE TABLE Orders (
   id serial PRIMARY KEY,
   cust_id INT REFERENCES Customers(id)
);

INSERT INTO Orders (cust_id) VALUES
    (1), (1), (1), (2), (2), (2),
    (5), (5), (5),  (6), (6), (6), 
    (7), (7), (7), (8), (8), (8), 
    (9), (9), (9);  

CREATE TABLE Categories (
    id serial PRIMARY KEY,
    category_name varchar(255) NOT NULL
);

INSERT INTO Categories (category_name) VALUES 
    ('Kitchen'),
    ('Electronics'),
    ('Gardening'),
    ('Toys'),
    ('Groceries'),
    ('Home Office');


CREATE TABLE Products (
    id serial PRIMARY KEY,
    product_name varchar(200) NOT NULL,
    inventory INTEGER,
    category_id INT REFERENCES Categories(id),
    product_cost FLOAT
);

INSERT INTO Products (product_name,inventory,category_id,product_cost) VALUES 
    ('Blender', 50, 1, 29.99), ('Microwave Oven', 30, 1, 99.99),
    ('Toaster', 60, 1, 19.99), ('Coffee Maker', 45, 1, 49.99),
    ('Dishwasher', 20, 1, 399.99),
    
    ('Smartphone', 100, 2, 499.99), ('Laptop', 40, 2, 899.99),
    ('Headphones', 150, 2, 79.99),('Smartwatch', 80, 2, 149.99),
    ('Bluetooth Speaker', 120, 2, 29.99),
    
    ('Garden Shovel', 70, 3, 14.99), ('Lawn Mower', 25, 3, 229.99),
    ('Plant Pots', 100, 3, 4.99),('Gardening Gloves', 80, 3, 9.99),
    ('Fertilizer', 50, 3, 19.99),
    
    ('Action Figure', 200, 4, 15.99),('Toy Car', 150, 4, 9.99),
    ('Building Blocks', 120, 4, 29.99),('Doll', 180, 4, 12.99),
    ('Toy Train Set', 50, 4, 79.99),
    
    ('Bread', 500, 5, 2.99),('Milk', 300, 5, 1.99),
    ('Eggs', 400, 5, 2.49),('Cheese', 200, 5, 4.99),
    ('Apples', 600, 5, 1.99),
    
    ('Desk', 50, 6, 89.99), ('Office Chair', 40, 6, 129.99),
    ('Laptop Stand', 150, 6, 29.99),('Desk Lamp', 70, 6, 19.99),
    ('File Cabinet', 30, 6, 149.99);

CREATE TABLE OrderItems (
    id serial PRIMARY KEY,
    order_id INT REFERENCES Orders(id),
    product_id INT REFERENCES Products(id),
    product_qty INT
);

INSERT INTO OrderItems (order_id, product_id, product_qty) VALUES
    (1, 1, 1), (1, 2, 2),
    (2, 5, 1), (2, 7, 3),
    (3, 12, 4), (3, 15, 2),
    (4, 20, 1), (4, 22, 5),
    (5, 30, 3), (5, 13, 2),
    (6, 25, 4), (6, 8, 1),
    (7, 10, 3), (7, 15, 2),
    (8, 13, 1), (8, 18, 2),
    (9, 19, 3), (9, 20, 4);