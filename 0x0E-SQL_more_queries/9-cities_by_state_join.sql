-- Write a script that lists all cities contained in the database 
SELECT cities.id, cities.name, states.name
FROM states, cities
WHERE cities.state_id = states.id
ORDER BY id ASC;
