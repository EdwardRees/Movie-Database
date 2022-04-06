from email import parser
from util import readFile

def parseRatings():
  ratings = []
  ratingsFile = readFile('../movies/ratings.txt')
  for line in ratingsFile.split('\n'):
    if line == '':
      continue
    line = line.split(":")
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
  with open('../out/ratings.txt', 'w') as f:
    for rating in ratings:
      f.write(f"{rating['userId']}::{rating['movieId']}::{rating['rating']}::{rating['timestamp']}\n")