-- Write a script that creates the database hbtn_0c_0
-- creates a table with id, score, and name
CREATE TABLE IF	NOT EXISTS second_table	(
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       score INT NOT NULL,
       PRIMARY KEY(id)
);

-- insert rows with values inside second_table
INSERT INTO second_table
       (id, name, score)
VALUES
	('1', 'John', '10'),
	('2', 'Alex', '3'),
	('3', 'Bob',  '14'),
	('4', 'George',	'8');
