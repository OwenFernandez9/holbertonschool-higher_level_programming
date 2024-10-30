-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.name AS genre,
COUNT(ts.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres ts ON tg.id = ts.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
