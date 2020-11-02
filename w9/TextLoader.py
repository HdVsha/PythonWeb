class DataConn:

    def __init__(self):
        self.path = None

    def __enter__(self):
        """
        Открываем подключение с потоком данных
        """
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """