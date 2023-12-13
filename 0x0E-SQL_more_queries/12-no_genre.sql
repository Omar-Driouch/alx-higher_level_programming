-- This query lists all the TV shows in the 'hbtn_0d_tvshows' database that are not associated with any genre.
-- It retrieves all rows from the database where the 'genre_id' column in the 'tv_show_genres' table is NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;