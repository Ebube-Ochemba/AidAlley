-- A script that prepares a MySQL server for the AidAlley project:
-- to use: "cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p"

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS aidalley_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'aidalley_user'@'localhost' IDENTIFIED BY 'aidalley_pwd';

-- Grant all privileges on the database aidalley_db to the user aidalley_user
GRANT ALL PRIVILEGES ON aidalley_db.* TO 'aidalley_user'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the user aidalley_user
GRANT SELECT ON performance_schema.* TO 'aidalley_user'@'localhost';

FLUSH PRIVILEGES;
