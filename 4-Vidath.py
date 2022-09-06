def max_heapify(A, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
max_heap(A)
n = len(A)
print("After sorting")
for i in range(n):
    print("%d " % A[i], end='')