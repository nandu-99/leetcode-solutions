import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semzero = threading.Semaphore(1)
        self.semeven = threading.Semaphore(0)
        self.semodd = threading.Semaphore(0)
        self.curr = 0 
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.semzero.acquire()
            printNumber(0)
            if self.curr%2==0:
                self.semodd.release()
            else:
                self.semeven.release()

        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.semeven.acquire()
            printNumber(i)
            self.curr+=1 
            self.semzero.release()

        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.semodd.acquire()
            printNumber(i)
            self.curr+=1 
            self.semzero.release()

        