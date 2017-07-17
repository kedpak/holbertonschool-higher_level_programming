-- script that lists all genres from hbtn_0d_tvshows
-- Each record should display: tv_genres.name - number of shows
-- Results must be sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_shows DESC;
