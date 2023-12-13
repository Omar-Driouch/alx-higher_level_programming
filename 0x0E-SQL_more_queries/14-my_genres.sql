-- This SQL query uses the 'hbtn_0d_tvshows' database to list all genres associated with the TV show 'Dexter'.
-- It performs a LEFT JOIN operation between the 'tv_genres', 'tv_show_genres', and 'tv_shows' tables based on the common 'id', 'genre_id', and 'show_id' columns respectively.
-- The result is grouped by genre name and ordered in ascending order.
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;