-- List all cities of California from the database hbtn_0d_usa.
-- This script retrieves all cities belonging to the state of California without using the JOIN keyword.

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id;
