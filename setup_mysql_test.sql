-- Creates Database 'hbnb_test_db'
-- Creates new user 'hbnb_test' with password 'hbnb_test_pwd' in localhost
-- Grants all privileges to the user on 'hbnb_tes_db' database
-- Grants SELECT previlege on 'perfomance_schema' database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
