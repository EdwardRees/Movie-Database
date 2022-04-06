from sys import argv
from movies import parseMovies, validateMovies, outputMovies
from genres import parseGenres, outputGenres
from tags import parseTags, validateTags, outputTags
from ratings import parseRatings, outputRatings
from download import prep
from users import Users


def main():
    prep()
    if(len(argv) < 1):
        print(
            "Invalid usage: `python3 files.py <print, io>`")
        return
    elif(argv[1] == 'print'):
        movies = parseMovies()
        invalidMovies = validateMovies(movies)
        if(len(invalidMovies) > 0):
            print("Invalid movies found. Update parser to handle the following cases:")
            print("Invalid movies:")
            for movie in invalidMovies:
                print(f"{movie['id']}:{movie['name']}")
        else:
            print(movies)
        genres = parseGenres()
        outputGenres(genres)
        tags = parseTags()
        invalidTags = validateTags(tags)
        if(len(invalidTags) > 0):
            print("Invalid tags found. Update parser to handle the following cases:")
            print("Invalid tags:")
            for tag in invalidTags:
                print(tag)
        else:
            print(tags)
        ratings = parseRatings()
        print(ratings)
    elif(argv[1] == 'io'):
        movies = parseMovies()
        invalidMovies = validateMovies(movies)
        if(len(invalidMovies) > 0):
            print("Invalid movies found. Update parser to handle the following cases:")
            print("Invalid movies:")
            for movie in invalidMovies:
                print(f"{movie['id']}:{movie['name']}")
        else:
            outputMovies(movies)
        genres = parseGenres()
        outputGenres(genres)
        tags = parseTags()
        invalidTags = validateTags(tags)
        if(len(invalidTags) > 0):
            print("Invalid tags found. Update parser to handle the following cases:")
            print("Invalid tags:")
            for tag in invalidTags:
                print(tag)
        else:
            outputTags(tags)
        ratings = parseRatings()
        outputRatings(ratings)
        Users.outputUsers()
    print("Done!")

if __name__ == '__main__':
    main()
