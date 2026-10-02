
import threading
from typing import Callable

class H2O:
    def __init__(self):
        self.semh = threading.Semaphore(2)
        self.semo = threading.Semaphore(0)
        self.lock = threading.Lock()
        self.count = 0

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.semh.acquire()
        releaseHydrogen()
        with self.lock:
            self.count += 1
            if self.count == 2:
                self.semo.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.semo.acquire()
        releaseOxygen()
        with self.lock:
            self.count = 0
            self.semh.release()
            self.semh.release()