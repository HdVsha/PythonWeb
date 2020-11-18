if __name__ == "__main__":
    import numpy as np
    import threading
    import matplotlib.pyplot as plt
    from datetime import datetime, timedelta

    def dot(v1, v2):
        return np.dot(v1, v2)

    def threaded_dot(array, thread):
        threads = []
        for attempt in range(thread):
            threads.append(threading.Thread(target=dot, args=(array[0], array[1],)))
            # threads.append(multiprocessing.Process(target=sum_a, args=(subarray, )))
            threads[-1].start()

        for thread_t in threads:
            thread_t.join(timeout=10)

        return "Finished dotting vectors"

    array_of_vecs = [[i**3 for i in range(1000000)] for j in range(2)]
    x_data = [1, 2, 4, 8, 10]  # Num of threads
    res_data = []
    for thread in x_data:
        tmp_data = []
        for sample in range(3):  # How many times to test this num of threads
            start = datetime.now()
            print(threaded_dot(array_of_vecs, thread))
            tmp_data.append((datetime.now() - start).microseconds)
        res_data.append(sum(tmp_data) / len(tmp_data))  # How much time did it take to proceed
    plt.plot(x_data, res_data)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число потоков')
    plt.show()
