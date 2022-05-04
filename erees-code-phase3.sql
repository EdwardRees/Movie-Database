-- Section A
-- 1
SELECT m.movieid,
  m.title,
  COUNT(r.userid)
FROM movies m,
  ratings r
WHERE m.movieid = r.movieid
GROUP BY m.movieid,
  m.title
ORDER BY COUNT(r.userid) DESC
LIMIT 1;
-- 2
SELECT m.movieid,
  m.title,
  COUNT(r.rating)
FROM movies m,
  ratings r
WHERE m.movieid = r.movieid
  AND r.rating = 5
GROUP BY m.movieid,
  m.title
ORDER BY COUNT(r.rating) DESC
LIMIT 1;
-- 3
SELECT COUNT(h1.movieid)
FROM has_genre h1,
  (
    SELECT movieid,
      COUNT(genre)
    FROM has_genre
    GROUP BY movieid
    HAVING COUNT(genre) > 4
  ) h2
WHERE h1.movieid = h2.movieid;
-- 4
SELECT genre,
  COUNT(movieid)
FROM has_genre
GROUP BY genre
ORDER BY COUNT(movieid) DESC
LIMIT 1;
-- 5
-- A
SELECT g.genre,
  g.high,
  g.low
FROM (
    (
      SELECT has_genre.genre,
        COUNT(ratings.rating) AS high
      FROM has_genre
        NATURAL JOIN ratings
      WHERE ratings.rating >= 4.0
      GROUP BY has_genre.genre
    ) g1
    NATURAL JOIN (
      SELECT has_genre.genre,
        COUNT(ratings.rating) AS low
      FROM has_genre
        NATURAL JOIN ratings
      WHERE ratings.rating < 4.0
      GROUP BY has_genre.genre
    ) g2
  ) g
ORDER BY g.high DESC;
-- B
SELECT g.genre,
  g.high,
  g.low
FROM (
    (
      SELECT has_genre.genre,
        COUNT(movies.year) AS high
      FROM has_genre
        NATURAL JOIN movies
      WHERE movies.year >= 2000
      GROUP BY has_genre.genre
    ) g1
    NATURAL JOIN (
      SELECT has_genre.genre,
        COUNT(movies.year) AS low
      FROM has_genre
        NATURAL JOIN movies
      WHERE movies.year < 2000
      GROUP BY has_genre.genre
    ) g2
  ) g
ORDER BY high DESC;
-- Section B
-- 1
INSERT INTO ratings_with_diff
SELECT r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg AS difference
FROM ratings r,
  (
    SELECT movieid,
      AVG(rating)
    FROM ratings
    GROUP BY movieid
  ) a
WHERE a.movieid = r.movieid
GROUP BY r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg;
-- 2
UPDATE ratings r
SET rating = rd.avg_rating,
  time = extract(
    epoch
    FROM current_timestamp at time zone ‘ utc ’
  )
FROM (
    SELECT userid,
      movieid,
      avg_rating,
      difference
    FROM ratings_with_diff
  ) rd
WHERE rd.userid = r.userid
  AND rd.movieid = r.movieid
  AND abs(rd.difference) > 3;
-- 3
CREATE TABLE ratings_with_diff2 (
  userid numeric,
  movieid numeric,
  rating double precision,
  “ time ” numeric,
  avg_rating double precision,
  difference double precision
);
INSERT INTO ratings_with_diff2
SELECT r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg AS difference
FROM ratings r,
  (
    SELECT movieid,
      AVG(rating)
    FROM ratings
    GROUP BY movieid
  ) a
WHERE a.movieid = r.movieid
GROUP BY r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg;
-- 4 
UPDATE ratings r
SET rating = rd.avg_rating,
  time = extract(
    epoch
    FROM current_timestamp at time zone ‘ utc ’
  )
FROM (
    SELECT userid,
      movieid,
      avg_rating,
      difference
    FROM ratings_with_diff2
  ) rd
WHERE rd.userid = r.userid
  AND rd.movieid = r.movieid
  AND abs(rd.difference) > 3;
CREATE TABLE ratings_with_diff3 (
  userid numeric,
  movieid numeric,
  rating double precision,
  “ time ” numeric,
  avg_rating double precision,
  difference double precision
);
INSERT INTO ratings_with_diff3
SELECT r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg AS difference
FROM ratings r,
  (
    SELECT movieid,
      AVG(rating)
    FROM ratings
    GROUP BY movieid
  ) a
WHERE a.movieid = r.movieid
GROUP BY r.userid,
  r.movieid,
  r.rating,
  r.time,
  a.avg,
  r.rating - a.avg;
UPDATE ratings r
SET rating = rd.avg_rating,
  time = extract(
    epoch
    FROM current_timestamp at time zone ‘ utc ’
  )
FROM (
    SELECT userid,
      movieid,
      avg_rating,
      difference
    FROM ratings_with_diff3
  ) rd
WHERE rd.userid = r.userid
  AND rd.movieid = r.movieid
  AND abs(rd.difference) > 3;
-- 5
SELECT m.title,
  m.movieid,
  ratings.orig AS original_rating,
  ratings.debiased AS debiased_rating,
  ratings.debiased - ratings.orig bias
FROM movies m,
  (
    SELECT original.movieid,
      original.avg_rating AS orig,
      final.avg_rating AS debiased
    FROM ratings_with_diff original
      INNER JOIN ratings_with_diff3 final USING (userid, movieid)
  ) ratings
WHERE ratings.movieid = m.movieid
GROUP BY m.movieid,
  m.title,
  ratings.orig,
  ratings.debiased
ORDER BY ratings.debiased - ratings.orig DESC
LIMIT 10;