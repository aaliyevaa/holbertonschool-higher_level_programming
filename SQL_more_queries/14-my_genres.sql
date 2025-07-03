-- Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE name = (
	SELECT tv_shows.title
	FROM tv_shows
	WHERE title = 'Dexter'
)
ORDER BY tv_genres.name;
