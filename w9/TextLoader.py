from zipfile import ZipFile
import os
import string


class TextLoader(ZipFile):

    def __init__(self, file, path):  # file - from where to extract, path - to where
        super().__init__(file)
        self.file_in_dir = None
        self.extractall(path)
        self.path = path
        self.path_of_file = path + "\sample"  # Now path to the files is stored in path

    def __enter__(self):
        """
        Открываем подключение с потоком данных
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.close()

    def __len__(self):
        file_count = len(os.listdir(self.path))
        return file_count

    def __iter__(self):
        return self

    def __next__(self):
        self.file_in_dir = next(iter(os.listdir(self.path)))
        file = self.path_of_file + self.file_in_dir
        try:
            f = open(file, 'r')
            for line in f:
                line.translate(str.maketrans('', '', string.punctuation))
                line.lower()
            copy_f = f
            f = open(file, 'w')
            f.write(str(copy_f))
            return f
        except StopIteration():
            raise StopIteration()
        finally:
            if f:  # Если файл не открылся, значит 'file' == None и закрывать его не нужно
                f.close()


if __name__ == "__main__":
    where_from = r'C:/Users/User/Downloads/sample.zip'
    where_to = r'C:\Users\User\PycharmProjects\MIPTStudies\w9\Archive'
    text_loader = TextLoader(where_from, where_to)
    print(len(text_loader))
    counter = 0
    for file in text_loader:
        counter += 1
    print(counter)
