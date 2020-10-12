import sys
import time
import datetime

def to_log(path):
    def decorator(func):
        def wrapper(*args):
            start = time.time()
            func(*args)
            finish = time.time()
            nores = '-'
            with open(path, 'w') as file:
                file.writelines(str(datetime.datetime.fromtimestamp(start)))
                file.writelines('\n')
                file.writelines(str(args))
                file.writelines('\n')
                file.writelines(nores)
                file.writelines('\n')
                file.writelines(str(datetime.datetime.fromtimestamp(start)))
                file.writelines('\n')
                file.writelines(str(round((finish - start), 5)))
                file.writelines('\n')
            return func(*args)
        return wrapper
    return decorator


@to_log('logfile.txt')
def some_func(a, b, c, d):
    print(sys.getsizeof(a))
    print(sys.getsizeof(b))
    print(sys.getsizeof(c))
    print(sys.getsizeof(d))
if __name__ == "__main__":
    some_func('haha', [1, 2, 4, 5, 6], (1, 2, 3, 5, 5, 6, 7, 7, 8, 8, 8), {1: ["hey"], 2: ["how r u doing, dude"]})
    with open('logfile.txt', 'r') as log:
        for line in log:
            print(line.strip())
