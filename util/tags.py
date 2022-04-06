from util import readFile

def parseTags():
  tags = []
  tagsFile = readFile("../movies/tags.txt")
  for line in tagsFile.split("\n"):
    if line == '':
      continue
    line = line.split(":")
    userId = line[0]
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
  invalidTags = []
  for line in tags:
    if len(line) != 4:
      print("Invalid tag:", line)
      invalidTags.append(line)
  return invalidTags

def outputTags(tags):
  with open("../out/tags.txt", "w") as f:
    for line in tags:
      f.write(f"{line['userId']}::{line['movieId']}::{line['tag']}::{line['timestamp']}\n")