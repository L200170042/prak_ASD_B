import tkinter      #tkinter merupan sarana gui dari python
import random
import tkinter.messagebox

#membuat root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="pink")

#Change the title
root.title("Aplikasi Antrian V.1")

#Change the window size
root.geometry("325x275")



##priorityqueue
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []     #menyimpan list inputan

    def __len__(self):
        return len(self.qlist)      #mengambil bnyak ny list di qlist

    def isEmpty(self):
        return len(self) == 0

#menambahkan antrian
    def enqueue(self, task, prio):
        entry = _PriorityQEntry(task, prio)
        self.qlist.append(entry)
        
#mengeluarkan antrian
    def dequeue(self):
        print (self.qlist)
        n = []
        for i in self.qlist:
            n.append(i.prio)
        pos = n.index(min(n))
        self.qlist.pop(pos).item
        return pos

    def getlist(self):
        return self.qlist






#prioritas
class _PriorityQEntry(object):
    def __init__(self, task, prio):
        self.item = task
        self.prio = prio

    def __str__(self):
        t = self.item
        return t


#sinsertionsort
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.prio < A[pos - 1].prio:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

# Program pencarian beruntun
def pencarian(A, target):
    a = 0
    for i in range(len(A)):
        if A[i].item == target:
            a+=i
    return a+1





# membuat priority queue
heu = PriorityQueue()


#==============================Create functions==================================


def update_listbox():
    lb_tasks.delete(0, "end")
    lb_prios.delete(0, "end")
    #Populate the listbox
    for x in heu.qlist:
        lb_tasks.insert("end", x.item)  #menampilkan list dari task
        lb_prios.insert("end", x.prio)  #menampilkan list dari prio
    
        


def add_task():
    #mengambil inputan
    task = txt_input.get()
    prio = txt_input_pr.get()
    #memasukan inputan kedalam antrian
    if task !="":
        #memasukan ke antrian
        heu.enqueue(task,prio)
        
        

    #Update the listbox
    update_listbox()

    txt_input.delete(0, "end")
    txt_input_pr.delete(0, "end")

def del_one():
    #mengeluarkan antrian sesuai prioritas terkecil
    p = heu.dequeue()
    lb_tasks.delete(p, "end")
    lb_prios.delete(p, "end")

    #Update the listbox
    update_listbox()

def sort_asc():
    #Sort the list
    insertionSort(heu.qlist)
    

    #Update the listbox
    update_listbox()

def sort_desc():
    #Sort the list
    insertionSort(heu.qlist)
    #Reverse the list
    heu.qlist.reverse()
    #Update the listbox
    update_listbox()

def btn_search():
    tasks2 = txt_input.get()
    a=pencarian(heu.qlist, tasks2)
    b=print(heu.qlist)
    if tasks2 == "":
        tkinter.messagebox.showwarning("Warning", "Please enter the keyword!")
    if tasks2 != "":
        message = tasks2,"Antrian Ke %a" %a
        lbl_display["text"] = message
    txt_input.delete(0, "end")
    










lbl_title = tkinter.Label(root, text="ANTRIAN", bg="pink")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", fg="black", bg="pink")
lbl_display.grid(row=10)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=0)

txt_input_pr = tkinter.Entry(root, width=5)
txt_input_pr.grid(row=1,column=1)

##tombol
btn_add_task = tkinter.Button(root, text="Antri", fg="black", bg="white", command=add_task)
btn_add_task.grid(row=1,column=2)


btn_del_one = tkinter.Button(root, text="Masuk", fg="black", bg="white", command=del_one)
btn_del_one.grid(row=3,column=2)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="black", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=2)

btn_sort_desc = tkinter.Button(root, text="Sort (DESC)", fg="black", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=2)

btn_search = tkinter.Button(root, text="Search", fg="black", bg="white", command = btn_search)
btn_search.grid(row=2,column=2)

btn_exit = tkinter.Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_exit.grid(row=8,column=2)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=0, rowspan=7)

lb_prios = tkinter.Listbox(root)
lb_prios.grid(row=2,column=1, rowspan=7)

#Start the main events loop
root.mainloop()



