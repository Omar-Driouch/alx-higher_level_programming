-- This SQL query retrieves all TV shows and their associated genres from the 'hbtn_0d_tvshows' database.
-- It performs a LEFT JOIN operation between the 'tv_shows', 'tv_show_genres', and 'tv_genres' tables based on the common 'id', 'show_id', and 'genre_id' columns respectively.
-- The result is ordered by the title of the TV show in ascending order, and then by the genre name in ascending order.
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;