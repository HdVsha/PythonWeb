class UnneededError(Exception):
    pass


if __name__ == "__main__":
    raise UnneededError("Error happened")