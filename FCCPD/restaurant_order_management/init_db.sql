-- Criação das tabelas
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
);

CREATE TABLE dishes (
    dish_id SERIAL PRIMARY KEY,
    dish_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    dish_id INT REFERENCES dishes(dish_id),
    quantity INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Pendente' -- Adiciona a coluna status com valor padrão
);

INSERT INTO customers (customer_name) VALUES 
('John Doe'), ('Jane Smith'), ('Alice Johnson'), 
('Bob Brown'), ('Charlie Black'), ('Diana White');

INSERT INTO dishes (dish_name, price) VALUES 
('Pizza', 9.99), ('Burger', 7.99), ('Pasta', 8.99), 
('Salad', 5.99), ('Soup', 4.99), ('Steak', 14.99);

INSERT INTO orders (customer_id, dish_id, quantity) VALUES
(1, 1, 2), (2, 3, 1), (3, 2, 4), 
(4, 5, 1), (5, 4, 3), (6, 6, 1);
