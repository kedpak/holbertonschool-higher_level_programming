-- Write a script that lists all the cities of California
-- Lists all fields with state_id of 1 (california)
SELECT `id`, `name` FROM hbtn_0d_usa.cities  WHERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = "California") ORDER BY hbtn_0d_usa.cities.id ASC;
