import time

class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1 # n1 == 0
        elif self.counter == 1:
            self.counter += 1
            return self.n2 # n2 == 1
        else:
            self.aux = self.n1 + self.n2 # aux == 0 + 1
        #       This is the same as Swapping
            # self.n1 = self.n2 # n1 == 1
            # self.n2 = self.aux # n2 == 1
        #       Swapping is the sugar syntax of the code above
            self.n1, self.n2 = self.n2, self.aux
            self.counter +=1
            return self.aux


# def run():
#     pass


if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)