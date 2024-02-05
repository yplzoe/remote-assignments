CREATE DATABASE assignment;
USE assignment;
CREATE TABLE user (
	id int PRIMARY KEY AUTO_INCREMENT, 
    email varchar(255),
    password varchar(255)
    );
SHOW COLUMNS FROM assignment.user;