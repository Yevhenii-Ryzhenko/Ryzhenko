class ReverseIteratorForList:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]



my_list = [1, 2, '1', 'f', True, {1:2}, (3,6,3,2), 8]

for item in ReverseIteratorForList(my_list):
    print(item)