-- List all cities along with their corresponding states from the database hbtn_0d_usa.
-- This script retrieves all cities with their state names in a single SELECT statement.

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
