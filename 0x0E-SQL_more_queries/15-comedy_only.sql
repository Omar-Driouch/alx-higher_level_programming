-- This query retrieves all TV shows from the 'hbtn_0d_tvshows' database that are categorized under the 'Comedy' genre.
-- It performs a LEFT JOIN operation between the 'tv_shows', 'tv_show_genres', and 'tv_genres' tables based on the common 'id', 'show_id', and 'genre_id' columns respectively.
-- The result is grouped by the title of the TV show and ordered in ascending order.
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;