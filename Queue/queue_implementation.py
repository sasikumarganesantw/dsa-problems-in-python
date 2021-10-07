class Queue:
    def __init__(self):
        self.queue = [];

    def insert(self, element):
        self.queue.append(element);
        return True;

    def traverse(self):
        if (len(self.queue)):
            for element in self.queue:
                print(element);
        else:
            print('Empty queue');
        return True;

    def remove(self):
        if (len(self.queue)):
            self.queue.remove(self.queue[0]);
        else:
            print('Empty queue');
        return True;

if __name__ == "__main__":
    queue = Queue()
    queue.insert(3)
    queue.insert(6)
    queue.insert(8)
    queue.insert(7)
    queue.traverse()
    queue.remove()
    print()
    queue.traverse()
    queue.remove()
    print()
    queue.traverse()
    queue.remove()
    print()
    queue.traverse()
    queue.remove()
    print()
    queue.traverse()