import zipfile
import os
from pathlib import Path

# file = zipfile.ZipFile(r"C:\Users\User\Downloads\main.zip")
# file.extractall(r"C:\Users\User\PycharmProjects\MIPTStudies")
with zipfile.ZipFile(r'C:\Users\User\Downloads\main.zip', 'r') as file:
    file.extractall(path=r"C:\Users\User\PycharmProjects\MIPTStudies\zippedfile")
ourlist = set()
our_p = Path(r"C:\Users\User\PycharmProjects\MIPTStudies\zippedfile")
for current_dir, dirs, files in os.walk(our_p):
    for file in files:
        if file.endswith('.py'):
            ourlist.add(current_dir)
ourlist = list(ourlist)
ourlist.sort()
for elem in ourlist:
    word = elem[-5] + elem[-4] + elem[-3] + elem[-2] + elem[-1]
    print(word)

