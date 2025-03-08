-- List all TV shows with at least one genre linked from the database hbtn_0d_tvshows.
-- This script retrieves the show titles and their corresponding genre IDs.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
