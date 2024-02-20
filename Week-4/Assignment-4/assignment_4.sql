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
SELECT us.id, ar.*
FROM (SELECT * FROM user ORDER BY id LIMIT 6, 6) as us
INNER JOIN article as ar
ON ar.email=us.email;