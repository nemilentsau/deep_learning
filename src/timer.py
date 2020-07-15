import time
import numpy as np

class Timer: #@save
    def __init__(self):
        # initialize the timer
        self.times = []
        self.start()

    def start(self):
        # start the timer
        self.tik = time.time()

    def stop(self):
        # stop timer and save recorded time into the list
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def sum(self):
        # returns sum of times
        return sum(self.times)

    def avg(self):
        # returns average time
        return self.sum()/len(self.times)

    def cumsum(self):
        # returns cumulative sum
        return np.array(self.times).cumsum().tolist()



