-- MySQL server setup for the AirBnB_v2 project
-- creates a database hbnb_dev
-- creates a new user 'hbnb_dev' without 'hbnb_dev_pwd' as password
-- The user has all previleges on the database 'hbnb_dev_db' only
-- the user has SELECT previlege on the dataase 'perfomance_schema' only

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
