from util import readFile

def parseGenres():
  genreList = []
  moviesFile = readFile('../movies/movies.txt')
  count = 1
  # Format: movieId:movieName (year):genre1|genre2|genre3
  for line in moviesFile.split("\n"):
    if line == '':
      continue
    line = line.split(":")
    movieId = line[0]
    genres = line[-1].split("|")
    for genre in genres:
      genreList.append({
        'id': count,
        'movieId': movieId,
        'genre': genre
      })
      count+=1
  return genreList



def outputGenres(genres):
  with open('../out/genres.txt', 'w') as f:
    for genre in genres:
      f.write(f"{genre['id']}::{genre['movieId']}::{genre['genre']}\n")
