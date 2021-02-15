from pygame import time

class Timer():

    clock = time.Clock()

    def __init__(self):
        self.reset_time()

    def update_time(self):
        self.time += self.clock.tick()

    def reset_time(self):
        self.time = 0





