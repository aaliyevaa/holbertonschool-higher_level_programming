-- List all cities of California
SELECT id, name, state_id
FROM cities
WHERE state_id = (
	SELECT states.id FROM states WHERE name = 'California' LIMIT 1
)
ORDER BY cities.id ASC;
