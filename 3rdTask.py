import zipfile
import os
from pathlib import Path


def write(array, file_name):
    array = map(lambda x: x + '\n', array)
    file_name.writelines(array)


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
with open("file_3task", "w") as ourfile:
    write(ourlist, ourfile)
with open("file_3task", "r") as file3:
    for line in file3:
        line = line.strip()
        print(line[-5] + line[-4] + line[-3] + line[-2] + line[-1])
