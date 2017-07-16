-- Write a script that creates the table
-- creates table force_name with id and name fields
CREATE TABLE IF NOT EXISTS force_name (
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id)
);
