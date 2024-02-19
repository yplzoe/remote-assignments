USE assignment;
-- CREATE TABLE article (
-- 	-- id int PRIMARY KEY AUTO_INCREMENT, 
-- 	author varchar(255),
--     email varchar(255),
--     title varchar(255),
--     content LONGTEXT
-- );

-- 1. select all articles with author's email
SELECT * FROM article;
-- 2. select articles from 7th to 12th sorted by id
SELECT ar.*, us.id
	FROM article as ar
	INNER JOIN user AS us
    ON ar.email=us.email
    WHERE us.id>=7 and us.id<=12;