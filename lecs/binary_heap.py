
class Binary_heap_v1:
    heap = []
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap[len(self.heap):] = [value]

    def remove_min:
        for i in range(len(self.heap)):
            if self.heap[i] == min(self.heap):
                self.heap.pop(i)
                break

class Binary_heap:
    heap = []
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap[len(self.heap):] = [value]
    while self.heap.index(value) > 0 and self.heap[self.heap.index(value)] < self.heap[(self.heap.index(value) -1) // 2]:
        self.heap[self.heap.index(value)], self.heap[(self.heap.index(value) - 1) // 2] = self.heap[(self.heap.index(value) - 1) // 2], self.heap[self.heap.index(value)]
        

    def remove_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        i = 0
        while (2 * i + 1) < len(self.heap):
            j = 2 * i + 1
            if (2 * i + 2) < len(self.heap) and self.heap[2 * i + 2] < self.heap[j]:
                j = 2 * i + 2
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
        return self.heap[-1]

    def __str__(self):
        return str(self.heap)
