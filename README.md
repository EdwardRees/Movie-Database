# Movie-Database
CS 333 Movie Database

## Dependencies

- PostgresSQL
- python3
- wget
- python3-wget

## Instructions to run

### Manual Running

1. Check if `wget`, `python3`, `pip3`, and the `wget` module in `pip3`
2. Enter the `util` folder and run the `files.py` script with `python3 files.py`<sup>[1]</sup>
3. Once the `files.py` finishes running, create a database in postgres called `moviesdb` either with `createdb moviesdb` or `psql -c "CREATE DATABASE moviesdb"`.
4. Once the database is created, run the `db.sql` script in postgres with the command `psql moviesdb < db.sql`. <sup>[2]</sup>

### Automated Running

- If the user is on Mac OS, they can run the `run.sh` script after changing the permissions to executable with `chmod +x run.sh`. This will automatically check for the dependencies - letting the user know if a dependency is missing or not, then run the python files. Afterwards, it'll check if the `moviesdb` database exists, if it doesn't, it will create the database. It will then run the `db.sql` script using `psql moviesdb < db.sql`.

### Footnotes
<sup>[1]</sup> This will download the `movies.zip` file, store it in a `movies` folder, which will be created if it doesn't already exist, then `unzip` the file. Once this is completed, it will parse the `movies.txt` file, creating the files `movies.txt` and `genres.txt`, placing them in the `out` folder - which would also be created if it doesn't already exist. The program will then read the `tags.txt` file, parse the contents, before creating a `tags.txt` file in the `out` folder. Lastly, it will read the `ratings.txt` file, parsing and creating a `ratings.txt` file placed in the `out` folder. While the `tags` and `ratings` are being parsed, a `Users` set is being generated, which eventually creates the `users.txt` file, keeping track of the `user id`s, which is also stored in the `out` folder.
<sup>[2]</sup> The `db.sql` file will drop the tables if they already exist, before reading the files in `out` and populating the tables from there.
