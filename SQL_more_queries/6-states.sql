-- This script creates a database hbtn_0d_usa and the table states inr MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
Use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(PRIMARY KEY (id), id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
