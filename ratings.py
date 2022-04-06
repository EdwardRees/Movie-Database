from util import readFile
from constants import DELIM1, DELIM2
from users import Users

def parseRatings():
  print("Parsing ratings...")
  ratings = []
  ratingsFile = readFile('./movies/ratings.txt')
  for line in ratingsFile.split('\n'):
    if line == '':
      continue
    line = line.split(":")
    Users.addToUsers(line[0])
    userId = line[0]
    movieId = line[1]
    rating = line[2]
    timestamp = line[3]
    ratings.append({
      'userId': userId,
      'movieId': movieId,
      'rating': rating,
      'timestamp': timestamp,
    })
  return ratings

def outputRatings(ratings):
  print("Writing ratings...")
  with open('./out/ratings.txt', 'w') as f:
    for rating in ratings:
      f.write(f"{rating['userId']}{DELIM2}{rating['movieId']}{DELIM2}{rating['rating']}{DELIM2}{rating['timestamp']}\n")