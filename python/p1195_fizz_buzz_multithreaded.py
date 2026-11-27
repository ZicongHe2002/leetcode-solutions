from threading import Condition


class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.condition = Condition()

    def run(self, predicate, output):
        with self.condition:
            while self.current <= self.n:
                if not predicate(self.current):
                    self.condition.wait()
                    continue
                output(self.current)
                self.current += 1
                self.condition.notify_all()

    def fizz(self, printFizz):
        self.run(lambda value: value % 3 == 0 and value % 5 != 0, lambda value: printFizz())

    def buzz(self, printBuzz):
        self.run(lambda value: value % 5 == 0 and value % 3 != 0, lambda value: printBuzz())

    def fizzbuzz(self, printFizzBuzz):
        self.run(lambda value: value % 15 == 0, lambda value: printFizzBuzz())

    def number(self, printNumber):
        self.run(lambda value: value % 3 != 0 and value % 5 != 0, printNumber)
