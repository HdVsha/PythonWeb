if __name__ == "__main__":
    '''
    Good pinging
    '''
    import os
    import threading

    def ping(host):
        print("... pinging ", host)
        ping_out = os.popen("ping " + host, "r")  # bufsize = 10 bytes
        while True:
            line = ping_out.readline()
            if not line:
                break
            print(line)

    ips = ['google.com',
           'wikipedia.org',
           'mipt.ru',
           'vk.com',
           'facebook.com']

    threads = [threading.Thread(target=ping, args=(ip,)) for ip in ips]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()



