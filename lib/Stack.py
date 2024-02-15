class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() != 0:
            return False
        else:
            return True

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            value = self.items[-1]
            del self.items[-1]
            return value

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit:
            return True
        else:
            return False

    def search(self, target):
        depth = 0
        while depth != self.size():
            if self.items[0 - (depth + 1)] == target:
                return depth
            else:
                depth += 1
        return -1
