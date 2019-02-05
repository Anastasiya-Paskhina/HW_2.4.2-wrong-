from datetime import datetime


class Session:
    def __enter__(self):
        print('Время запуска {}'.format(datetime.now().time()))
        self.start_time = datetime.now()
        return self

    def __exit__(self, *args):
        print('Время окончания работы {}'.format(datetime.now().time()))
        self.end_time = datetime.now()
        self.process_time = self.end_time - self.start_time
        print('Код был выполнен за: {}'.format(self.process_time))