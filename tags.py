from util import readFile
from constants import DELIM1, DELIM2
from users import Users

def parseTags():
  print("Parsing tags...")
  tags = []
  tagsFile = readFile("./movies/tags.txt")
  for line in tagsFile.split("\n"):
    if line == '':
      continue
    line = line.split(":")
    userId = line[0]
    Users.addToUsers(userId)
    movieId = line[1]
    timestamp = line[-1]
    tag = ':'.join(line[2:-1])
    tags.append({
      'userId': userId,
      'movieId': movieId,
      'timestamp': timestamp,
      'tag': tag
    })
  return tags

def validateTags(tags):
  print("Validating tags...")
  invalidTags = []
  for line in tags:
    if len(line) != 4:
      print("Invalid tag:", line)
      invalidTags.append(line)
  return invalidTags

def outputTags(tags):
  print("Writing tags...")
  with open("./out/tags.txt", "w") as f:
    for line in tags:
      f.write(f"{line['userId']}{DELIM2}{line['movieId']}{DELIM2}{line['tag']}{DELIM2}{line['timestamp']}\n")