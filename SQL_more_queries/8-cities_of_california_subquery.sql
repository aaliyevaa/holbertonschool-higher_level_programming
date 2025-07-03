-- List all cities of California
SELECT id, name, state_id
FROM cities
WHERE state_id = (
	SELECT id FROM states WHERE name = 'California' LIMIT 1
)
ORDER BY id ASC;
