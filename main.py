class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.method_called = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def method_called(self):
        self.method_called += 1
        return self.method_called
