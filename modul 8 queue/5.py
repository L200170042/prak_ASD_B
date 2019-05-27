class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


heu = PriorityQueue()
heu.enqueue('Gajah', 3)
heu.enqueue('Jangkrik', 1)
heu.enqueue('Semut', 0)
heu.enqueue('Paus', 4)
heu.enqueue('Kucing', 2)

print (heu.dequeue())
print (heu.dequeue())
print (heu.dequeue())
print (heu.dequeue())
print (heu.dequeue())
