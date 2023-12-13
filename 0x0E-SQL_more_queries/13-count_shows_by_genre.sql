-- This SQL query lists all genres from the 'hbtn_0d_tvshows' database and displays the number of TV shows associated with each genre.
-- It retrieves all rows from the database where the 'genre_id' in the 'tv_show_genres' table matches the 'id' in the 'tv_genres' table.
-- The result is grouped by genre and ordered by the number of shows in descending order.
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;