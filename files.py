from sys import argv
from movies import parseMovies, validateMovies, outputMovies
from genres import parseGenres, outputGenres
from tags import parseTags, validateTags, outputTags
from ratings import parseRatings, outputRatings
from download import prep
from users import Users


def main():
    prep()
    if(len(argv) > 1):
      if(argv[1] == '-h'):
        print("Usage: python3 files.py [-h,-d]\n-h: help\n-d: debug. Will print out the values of the files parsed as the original list and dictionary values.\nIf no flag is passed, the program will continue with the default behavior of outputting the files to the output directory.")
        return
      elif(argv[1] == '-d'):
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
    else:
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
