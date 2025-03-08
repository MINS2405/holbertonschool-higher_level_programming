-- List all TV shows with their associated genre ID, including shows with no genre.
-- This script retrieves all show titles and their corresponding genre IDs, displaying NULL if no genre is linked.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
