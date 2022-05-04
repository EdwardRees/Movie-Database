#!/bin/bash
dropdb moviesdb;
createdb moviesdb;
psql moviesdb < moviesdb_dump_file;
psql moviesdb < create_ratings_with_diff.sql;
