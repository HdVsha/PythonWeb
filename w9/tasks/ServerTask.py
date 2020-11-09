class Connect(Exception):
    pass


class Write(Exception):
    pass


def connect_user(user_info):
    pass  # doing smth with info
    # command_planner().throw(Write)
    with open("file.txt", 'w') as f:
        yield from write_to_file(f)


def write_to_file(f_obj):
    while True:
        x = yield
        if x == "Stop":
            break
        f_obj.writelines(x)
        f_obj.writelines("\n")
    f_obj.close()


def command_planner():
    print("Work has started")
    auth = []
    while True:
        try:
            info = yield
            auth.append(info)
        except Connect:
            yield from connect_user(auth)


if __name__ == "__main__":
    coroutine = command_planner()
    next(coroutine)
    coroutine.send(["Ramil", "Ageev"])
    next(coroutine)
    coroutine.throw(Connect)
    coroutine.send("info")
    coroutine.send("something")
    coroutine.send("stop")

    coroutine.close()
