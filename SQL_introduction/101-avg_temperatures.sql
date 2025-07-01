-- Average temperature
SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
