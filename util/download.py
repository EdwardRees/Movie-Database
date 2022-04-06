from shutil import move
from os import mkdir, path
import wget
import zipfile

def prep():
  url = "https://www.dropbox.com/s/2rn7qc51yvmb766/movies.zip?dl=1"
  movieszip = wget.download(url, 'movies.zip')
  print(movieszip)

  path.isdir('../out') or mkdir('../out')
  path.isdir("../movies") or mkdir("../movies")

  move(movieszip, "../movies/movies.zip")

  print("Extracting movies.zip...")
  with zipfile.ZipFile("../movies/movies.zip", 'r') as zip_ref:
    zip_ref.extractall("../movies")

  print("Done!")

if __name__ == '__main__':
  prep()