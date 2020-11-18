import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def dot(v1, v2):
    return np.dot(v1, v2)


def split_array(v1, v2, pieces_number):
    res_v1, res_v2 = np.split(np.array(v1), pieces_number), np.split(np.array(v2), pieces_number)

    for i in range(len(res_v1)):
        if res_v1[i].size > 0:
            yield (res_v1[i], res_v2[i])


def processed_dot(mas, th):
    processes = []
    for subarray1, subarray2 in split_array(mas[0], mas[1], th):
        processes.append(multiprocessing.Process(target=dot, args=(np.array(subarray1), np.array(subarray2),)))
        processes[-1].start()
    for process in processes:
        process.join()

    return "Finished dotting vectors"


if __name__ == "__main__":

    array_of_vecs = [[i ** 3 for i in range(10000000)] for j in range(2)]
    x_data = [1, 2, 4, 8, 10]  # Num of threads
    res_data = []
    for thread in x_data:
        tmp_data = []
        for sample in range(3):  # How many times to test this num of threads
            start = datetime.now()
            print(processed_dot(array_of_vecs, thread))
            tmp_data.append((datetime.now() - start).microseconds)
        res_data.append(sum(tmp_data) / len(tmp_data))  # How much time did it take to proceed
    plt.plot(x_data, res_data)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число процессов')
    plt.show()

