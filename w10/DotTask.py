if __name__ == "__main__":
    import numpy as np
    import threading

    def dot(v1, v2):
        return np.dot(v1, v2)

    a, b = [i*2 for i in range(10)], [i for i in range(10)]

    threads = [threading.Thread(target=dot, args=(a, b,))]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()




