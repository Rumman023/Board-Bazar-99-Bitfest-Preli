--Using SQL 
-- New Database 
CREATE DATABASE kitchen_buddy;
USE kitchen_buddy;

--Table for storing information of the available ingredients
CREATE TABLE Ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity FLOAT NOT NULL,
    unit VARCHAR(50),
    category VARCHAR(100),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table containing the recipes
CREATE TABLE Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ingredients TEXT NOT NULL,
    cuisine VARCHAR(100),
    taste VARCHAR(100),
    prep_time INT,
    reviews TEXT
);


--Example insertions
INSERT INTO Ingredients (name, quantity, unit, category)
VALUES ('Sugar', 2.5, 'kg', 'Baking'),
       ('Milk', 1, 'liters', 'Dairy'),
       ('Eggs', 12, 'pcs', 'Protein');
INSERT INTO Recipes (name, ingredients, cuisine, taste, prep_time, reviews)
VALUES ('Pancakes', '[{"name": "Flour", "quantity": "2 cups"}, {"name": "Milk", "quantity": "1 cup"}, {"name": "Eggs", "quantity": "2 pcs"}]', 'American', 'Sweet', 15, 'Delicious and easy to make!');
