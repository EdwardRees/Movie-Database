from util import readFile
from constants import DELIM1, DELIM2

def parseMovies():
  print("Parsing movies...")
  movies = []
  genres = []
  moviesFile = readFile('../movies/movies.txt')
  for line in moviesFile.split('\n'):
    if line == '':
      continue
    line = line.split(":")
    movieId = line[0]
    genres = line[-1].split("|")
    movieName = ':'.join(line[1:-1])
    movieYear = movieName.split("(")[-1].split(")")[0]
    movieName = movieName.replace(f"({movieYear})", "")
    movieName = movieName.strip()
    movies.append({
      'id': movieId,
      'name': movieName,
      'year': movieYear,
    })
  return movies

def validateMovies(movies):
  print("Validating movies...")
  invalidMovies = []
  for movie in movies:
    if movie['year'] == '':
      print(f"{movie['id']}:{movie['name']}")
      invalidMovies.append(movie)
    if f"({movie['year']})" in movie['name']:
      print(f"{movie['id']}:{movie['name']}")
      invalidMovies.append(movie)
    try:
      int(movie['year'])
    except ValueError:
      invalidMovies.append(movie)
      print(movie['name'])
  return invalidMovies


def outputMovies(movies):
  print("Writing movies...")
  with open('../out/movies.txt', 'w') as f:
    for movie in movies:
      f.write(f"{movie['id']}{DELIM1}{movie['name']}{DELIM1}{movie['year']}\n")
