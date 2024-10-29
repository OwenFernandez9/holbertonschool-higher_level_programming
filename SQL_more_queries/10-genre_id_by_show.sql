-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_show.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;