CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    role VARCHAR(50)
);

INSERT INTO users (name, email, role) VALUES
('Sai', 'sai@example.com', 'DevOps Engineer'),
('Ganesh', 'ganesh@example.com', 'Backend Developer');
