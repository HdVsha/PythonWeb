def write (array, file_name):
    with open(file_name, 'w') as out:
        out.writelines(array)
    pass
array = ["ksk","sda","dasda"]
write(array,"2.txt")