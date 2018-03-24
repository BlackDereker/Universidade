import time


class StopWatch(object):

    before = 0
    after = 0

    def start(self):
        self.before = time.time() * 1000

    def stop(self):
        self.after = time.time() * 1000

    def reset(self):
        self.before = 0

    def currentValue(self):
        return (time.time() * 1000) - self.before

    def storedValue(self):
        return self.after - self.before
