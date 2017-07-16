-- Write a script that creates the database and user
-- Creates user user_0d_2 and sets privilege to SELECT
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
