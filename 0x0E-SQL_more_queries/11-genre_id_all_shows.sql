-- This query retrieves all TV shows and their associated genre IDs from the 'hbtn_0d_tvshows' database.
-- It performs a LEFT JOIN operation between the 'tv_shows' and 'tv_show_genres' tables based on the common 'id' and 'show_id' columns respectively.
-- The result is ordered by the title of the TV show in ascending order, and then by the genre ID in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;