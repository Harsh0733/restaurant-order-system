CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS customer_orders;

CREATE TABLE menu (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50),
    category ENUM('Starter', 'MainCourse', 'Dessert'),
    price DECIMAL(10,2)
);

CREATE TABLE customer_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    table_number INT,
    item_name VARCHAR(50),
    category VARCHAR(20),
    price DECIMAL(10,2),
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO menu (item_name, category, price) VALUES
('Panner Tika', 'Starter', 120),
('Malai Broccoli', 'Starter', 130),
('Mushroom Tika', 'Starter', 110),
('Paneer Manchurian', 'Starter', 140),
('Veg Manchurian', 'Starter', 135),
('Veg BBQ', 'Starter', 150),
('Paneer Masala', 'MainCourse', 180),
('Butter Panner', 'MainCourse', 190),
('Mushroom Mix', 'MainCourse', 170),
('Tandoori Grilled Pomfret', 'MainCourse', 250),
('Surmai Delight', 'MainCourse', 260),
('Spl. Anglo Chicken', 'MainCourse', 270),
('Butter Naan', 'MainCourse', 40),
('Tandoori Naan', 'MainCourse', 50),
('Garlic Naan', 'MainCourse', 50),
('Jeera Rice', 'MainCourse', 60),
('Steam Rice', 'MainCourse', 55),
('Mix Veg Kulcha', 'MainCourse', 65),
('Chocolate Hazelnut', 'Dessert', 90),
('Chikki Cheesecake', 'Dessert', 95),
('Chikki Baklava', 'Dessert', 100),
('Large Donuts', 'Dessert', 80),
('Hazelnut Cappuccino', 'Dessert', 120),
('Chocolate Ice Cream', 'Dessert', 70);
