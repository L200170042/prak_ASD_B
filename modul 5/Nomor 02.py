def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

A = [1,2,3,4,5,8,11,13,14,15]
B = [6,7,9,10,12,16,18,20,22]
C = []
C.extend(A)
C.extend(B)
print ('Nilai C' , C)
