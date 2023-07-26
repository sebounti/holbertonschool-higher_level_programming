-- This script lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT TV_SHOWS.title, TV_SHOW_GENRES.genre_id
	FROM TV_SHOWS
		LEFT JOIN TV_SHOW_GENRES
		ON TV_SHOWS.id = TV_SHOW_GENRES.show_id
		WHERE TV_SHOW_GENRES.genre_id IS NULL
ORDER BY TV_SHOWS.title, TV_SHOW_GENRES.genre_id;
