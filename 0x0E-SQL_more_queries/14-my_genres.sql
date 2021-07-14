-- Use the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_shows.title = 'Dexter' AND tv_show_genres.show_id = tv_shows.id
AND tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name;
