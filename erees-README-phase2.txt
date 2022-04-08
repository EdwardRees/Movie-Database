# Phase 2

Edward Rees

April 11 2022

CS 333: Introduction to Database Systems

Spring 2022

Design, Load, and Explore a Movies database

## Code info

Too many Python files to include in the submission. Python files are at the following Github repository, along with helper files.

Python Files at: https://github.com/EdwardRees/Movie-Database

- constants.py: Python code containing constants used
- download.py: Python code to download the movies.zip file, moving the zip file to a `movies` folder created, unzipping the file in the `movies` folder.
- files.py: Python code containing primary file parsing executions, calls other python functions
- genres.py: Python code to parse out the genres from the `movies.txt` file, creating the `genres.txt` and `has_genre.txt` files in the `out` folder
- ratings.py: Python code to parse out the ratings and create the `ratings.txt` file in the `out` folder
- tags.py: Python code to parse out the tags and create the `tags.txt` file in the `out` folder
- users.py: Python code to parse out the user ids and create the `users.txt` file in the `out` folder
- util.py: Python code to read a file and other simple utility functions

# Instructions for running the program:

## Manual Running:

1. Check if `wget`, `python3`, `pip3`, and the `wget` module in `pip3`
2. Enter the `util` folder and run the `files.py` script with `python3 files.py`<sup>[1]</sup>
3. Once the `files.py` finishes running, create a database in postgres called `moviesdb` either with `createdb moviesdb` or `psql -U postgres -c "CREATE DATABASE moviesdb"`.
4. Once the database is created, run the `db.sql` script in postgres with the command `psql moviesdb < db.sql`. <sup>[2]</sup>

## Automated Running:

- Pull the `run.sh` file from https://github.com/EdwardRees/Movie-Database and run the file.
- Follow the steps as outlined in the `README.md` file in the repository: https://github.com/EdwardRees/Movie-Database
