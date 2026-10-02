class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzsem = threading.Semaphore(0)
        self.buzzsem = threading.Semaphore(0)
        self.fizzbuzzsem = threading.Semaphore(0)
        self.numsem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i%3==0 and i%5!=0:
                self.fizzsem.acquire()
                printFizz()
                self.numsem.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i%5==0 and i%3!=0:
                self.buzzsem.acquire()
                printBuzz()
                self.numsem.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i%15==0:
                self.fizzbuzzsem.acquire()
                printFizzBuzz()
                self.numsem.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.numsem.acquire()
            if i%15==0:
                self.fizzbuzzsem.release()
            elif i%3==0:
                self.fizzsem.release()
            elif i%5==0:
                self.buzzsem.release()  
            else:
                printNumber(i)
                self.numsem.release()      