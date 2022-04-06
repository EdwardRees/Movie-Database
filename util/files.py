from sys import argv
from movies import parseMovies, validateMovies, outputMovies
from genres import parseGenres, outputGenres
from tags import parseTags, validateTags, outputTags
from ratings import parseRatings, outputRatings
from download import prep


def main():
    prep()
    if(len(argv) < 2):
        print(
            "Invalid usage: `python3 files.py <movies, genres, ratings, tags> <print, io>`")
        return
    if(argv[1] == 'movies'):
        movies = parseMovies()
        invalidMovies = validateMovies(movies)
        if(len(invalidMovies) > 0):
            print("Invalid movies found. Update parser to handle the following cases:")
            print("Invalid movies:")
            for movie in invalidMovies:
                print(f"{movie['id']}:{movie['name']}")
        else:
            if argv[2] == 'print':
                print(movies)
            elif argv[2] == 'io':
                outputMovies(movies)
    elif(argv[1] == 'genres'):
        genres = parseGenres()
        if argv[2] == 'print':
            print(genres)
        elif argv[2] == 'io':
            outputGenres(genres)
    elif(argv[1] == 'tags'):
        tags = parseTags()
        invalidTags = validateTags(tags)
        if(len(invalidTags) > 0):
            print("Invalid tags found. Update parser to handle the following cases:")
            print("Invalid tags:")
            for tag in invalidTags:
                print(tag)
        else:
            if argv[2] == 'print':
                print(tags)
            elif argv[2] == 'io':
                outputTags(tags)
    elif(argv[1] == 'ratings'):
        ratings = parseRatings()
        if argv[2] == 'print':
            print(ratings)
        elif argv[2] == 'io':
            outputRatings(ratings)
    elif(argv[1] == 'all'):
        movies = parseMovies()
        invalidMovies = validateMovies(movies)
        if(len(invalidMovies) > 0):
            print("Invalid movies found. Update parser to handle the following cases:")
            print("Invalid movies:")
            for movie in invalidMovies:
                print(f"{movie['id']}:{movie['name']}")
        else:
            if argv[2] == 'print':
                print(movies)
            elif argv[2] == 'io':
                outputMovies(movies)
        genres = parseGenres()
        if argv[2] == 'print':
            print(genres)
        elif argv[2] == 'io':
            outputGenres(genres)
        tags = parseTags()
        invalidTags = validateTags(tags)
        if(len(invalidTags) > 0):
            print("Invalid tags found. Update parser to handle the following cases:")
            print("Invalid tags:")
            for tag in invalidTags:
                print(tag)
        else:
            if argv[2] == 'print':
                print(tags)
            elif argv[2] == 'io':
                outputTags(tags)
        ratings = parseRatings()
        if argv[2] == 'print':
            print(ratings)
        elif argv[2] == 'io':
            outputRatings(ratings)


if __name__ == '__main__':
    main()
