-- Write a script that lists all the cities of California
-- Lists all fields with state_id of 1 (california)
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
