-- Prepares a MySQL server for the project by
-- Creating new DB hbnb_test_db and new user hbnb_test in localhost
-- psswd for user set to hbnb_test_pwd
-- grants all privileges to new user on db hbnb_test_db
-- grants select privileges to new user on db performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT USAGE ON *.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
