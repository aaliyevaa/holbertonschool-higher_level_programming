-- Comedy only
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.id
JOIN tv_genres ON tv_show_genres.id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER tv_shows.title;
