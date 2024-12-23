-- >- Retrieve the customers with a Gmail email address
SELECT (first_name, last_name) AS name, email_address FROM Customers
WHERE email_address LIKE '%gmail.%';


-- >- Retrieve the customers under 25 years old
SELECT (first_name, last_name) AS name, DATE_PART('years',AGE(dob)) AS Current_age FROM Customers
WHERE DATE_PART('years',AGE(dob)) < 25;

-- >- Retrieve customer ID 2's orders
SELECT id AS OrderId, cust_id FROM orders
WHERE cust_id = 2;


-- >- Retrieve customer ID 2's purchased products
SELECT product_name, cust_id FROM Products
JOIN OrderItems ON Products.id = OrderItems.product_id
JOIN  Orders ON orderItems.order_id = Orders.id
WHERE Orders.cust_id = 2;


-- >- Retrieve all the products under the "Home Office" category
SELECT product_name, category_name FROM Products
JOIN Categories ON category_id = Categories.id
WHERE categories.category_name = 'Home Office';


-- >- Retrieve all the orders that have a product which belongs to the "Kitchen" category
SELECT DISTINCT Orders.id AS Order_ID FROM Orders
JOIN OrderItems ON Orders.id = OrderItems.order_id
JOIN Products ON OrderItems.product_id = products.id
WHERE category_id = (
    SELECT id FROM categories WHERE category_name = 'Kitchen'
);