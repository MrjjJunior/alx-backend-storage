-- enumerartion of countries

CREATE TABLE IF NOT EXISTS users (
    id INT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

