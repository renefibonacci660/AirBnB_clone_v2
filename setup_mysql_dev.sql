-- Prepares a MySQL server for the project by
-- Creating new DB hbnb_dev_db and new user hbnb_dev in localhost
-- psswd for user set to hbnb_dev_pwd
-- grants all privileges to new user on db hbnb_dev_db
-- grants select privileges to new user on db performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT USAGE ON *.*
      TO `hbnb_dev`@`localhost`
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.*
      TO `hbnb_dev`@`localhost`
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.*
      TO `hbnb_dev`@`localhost`
      IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
