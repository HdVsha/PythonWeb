import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def q_dot(v1, v2, q):
    q.put(np.dot(v1, v2))
    return q


def count_res_dot(q):
    res = 0
    while q:
        res += q.get()
        print("suka")
    return res


def split_array(v1, v2, pieces_number):
    res_v1, res_v2 = np.split(v1, pieces_number), np.split(v2, pieces_number)
    for i in range(len(res_v1)):
        if res_v1[i].size > 0:
            yield (res_v1[i], res_v2[i])


def processed_dot(mas, pr, q):
    pool = multiprocessing.Pool(processes=pr)
    tmp_results = [pool.apply_async(q_dot, args=(subarray1, subarray2, q,))  # Only need what in [...]
                   for subarray1, subarray2 in split_array(mas[0], mas[1], pr)]


if __name__ == "__main__":

    queue = multiprocessing.Queue()
    arr_length = int(1e6)
    array_of_vecs = [np.random.randn(arr_length), np.random.randn(arr_length)]
    x_data = [1, 2, 4, 8, 10]  # Num of processes
    res_data = []
    for processes in x_data:
        tmp_data = []
        for sample in range(3):  # To see in average
            start = datetime.now()
            processed_dot(array_of_vecs, processes, queue)
            tmp_data.append((datetime.now() - start).microseconds)
        res_data.append(sum(tmp_data) / len(tmp_data))  # How much time did it take to proceed
    plt.plot(x_data, res_data)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число процессов')
    plt.show()

