import os

from game.file import File


FILES = [
    File("words/" + filename)
    for filename in os.listdir("words")
    if filename.endswith(".txt")
]
FILES.sort(key=lambda file: file.name)
if len(FILES) == 0:
    raise Exception("words folder is empty")
