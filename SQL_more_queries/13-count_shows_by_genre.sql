--
select tv_genre.name as genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genre
LEFT JOIN tv_show_genres ON tv_genre.id = tv_show_genres.genre_id
GROUP BY tv_genre.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;