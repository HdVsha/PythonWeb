import numpy as np


class Average(Exception):
    pass


class Disperse(Exception):
    pass


class Counter(Exception):
    pass


def real_time_handler():
    print("Work has started")
    info = []
    while True:
        try:
            x = yield
            print(f"The info given to the handler: {x}")
            info.append(x)
        except Disperse:
            yield np.var(info)
        except Counter:
            yield len(info)
        except Average:
            yield np.mean(info)


if __name__ == "__main__":

    coroutine = real_time_handler()
    next(coroutine)  # We need to enter the cycle ( "to start the vehicle" ) and set coroutine for waiting the value

    for i in range(20):

        coroutine.send(i)  # Sending the info through x = yield
        '''
        Testing the handler
        '''
        if i % 2 == 0:
            print("The disperse of info is: ", coroutine.throw(Disperse))
            next(coroutine)  # It is needed to go to the next key point in the program(because we send info with yield)
        if i % 3 == 0:
            print("The average of info is: ", coroutine.throw(Average))
            next(coroutine)
        if i % 5 == 0:
            print("The length of info is: ", coroutine.throw(Counter))
            next(coroutine)

    coroutine.close()  # Need to close the coroutine after finished work
