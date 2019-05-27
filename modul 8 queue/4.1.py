class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    
    ## 4.1 soal-soal untuk mahasiswa
    def getFrontMost(self):
        return self.qlist[0]

    ## 4.2 soal-soal untuk mahasiswa
    def getRearMost(self):
        return self.qlist[len(self.qlist) - 1]

heu = Queue()
heu.enqueue(1)
heu.enqueue(5)
heu.enqueue(12)
heu.enqueue(25)

print ('item paling depan = ', heu.getFrontMost())
print (heu.dequeue())
print (heu.dequeue())
print (heu.dequeue())
print (heu.dequeue())
