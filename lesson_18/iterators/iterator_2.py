class IteratorForEvenNumbers:

    def __init__(self, n):
        self.n = n
        self.current = 0


    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n: # включно з N
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

testing_iterator = IteratorForEvenNumbers(10)
for r in testing_iterator:
    print(r)

