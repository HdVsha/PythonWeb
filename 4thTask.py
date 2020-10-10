import argparse


def prime_numbers(n):
    try:
        n = int(n)
    except TypeError:
        print("Why do you convert it string to the number?")
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--show-all', action='store_true', default=False)
    parser.add_argument('-f', '--file', type=argparse.FileType('w', encoding='utf8'))
    parser.add_argument('number', type=int)  #благодаря этому, можем найти именно интовый аргумент
    return parser





if __name__ == "__main__":

    parser = createParser()
    args = parser.parse_args()

    primes_array = prime_numbers(args.number)
    last_prime = primes_array[-1]

    print(last_prime)

    if args.show_all:
        print(*primes_array)
        if args.file:
            print(*primes_array, file=args.file)

    if args.file:
        print(last_prime, file=args.file)
