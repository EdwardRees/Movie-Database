CREATE DATABASE moviesdb;
DROP TABLE IF EXISTS movies CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS genres;
CREATE TABLE movies(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  year INTEGER NOT NULL
);
CREATE TABLE users(id SERIAL PRIMARY KEY);
CREATE TABLE ratings(
  movieId INTEGER NOT NULL,
  userId INTEGER NOT NULL,
  rating FLOAT NOT NULL,
  ratingTime INTEGER,
  FOREIGN KEY (movieId) REFERENCES movies(id),
  FOREIGN KEY (userId) REFERENCES users(id)
);
CREATE TABLE tags(
  movieId INTEGER NOT NULL,
  userId INTEGER NOT NULL,
  tag TEXT NOT NULL,
  tagTime INTEGER,
  FOREIGN KEY(movieId) REFERENCES movies(id),
  FOREIGN KEY(userId) REFERENCES users(id)
);
CREATE TABLE genres(
  id SERIAL PRIMARY KEY,
  movieId INTEGER NOT NULL,
  genreTitle TEXT NOT NULL,
  FOREIGN KEY(movieId) REFERENCES movies(id)
);
\copy movies(id,title,year) FROM './out/movies.txt' DELIMITER ';';
\copy genres(id,movieId,genreTitle) FROM './out/genres.txt' DELIMITER ';';
\copy users(id) FROM './out/users.txt' DELIMITER ',';
\copy ratings(userId,movieId,rating,ratingTime) FROM './out/ratings.txt' DELIMITER ',';
\copy tags(userId,movieId,tag,tagTime) FROM './out/tags.txt' DELIMITER ',';