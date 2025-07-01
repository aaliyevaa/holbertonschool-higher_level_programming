-- Display the top 3 cities temperature
SELECT `city`, `value` AS `temperature`
FROM `temperatures`
WHERE `month` IN (7, 8)
ORDER BY `temperature` DESC
LIMIT 3;
