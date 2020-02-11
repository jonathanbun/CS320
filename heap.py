import sys
import math

# BEGIN DO NOT MODIFY

db = False
swap_count = 0
heapify_call_count = 0

array_length = 0 # ONCE SET FOR A GIVEN ARRAY, THIS SHOULD NEVER CHANGE
# EVEN WHEN DOING OPERATIONS LIKE EXTRACT-MIN AND HEAP-INSERT

n = 0 #length of the 'heap'. n <= array_length

def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0

def swap(A, i, j):
    global swap_count
    swap_count += 1
    A[i], A[j] = A[j], A[i]

def count_heapify():
    global heapify_call_count
    heapify_call_count += 1

def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}

def readNums(filename):
    """Reads a text file containing whitespace separated numbers.
    Returns a list of those numbers."""
    global array_length
    global n

    n = 0 # set initial heap length to 0
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        array_length = len(lst)

        if db:
            print("List read from file {}: {}".format(filename, lst))
            print("array_length = {}".format(array_length))

        return lst

def shuffled_list(length, seed):
    global array_length
    global n

    lst = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(lst)
    array_length = len(lst)
    n = 0 # set initial heap length to 0
    return lst

def printCompleteTree(A):
    """ A handy function provided to you, so you can see a
    complete tree in its proper shape.
    Note that this function shows the ENTIRE ARRAY in the form of a tree
    """

    height = int(math.log(len(A), 2))
    width = len(str(max(A)))
    for i in range(height + 1):
        print(width * (2 ** (height - i) - 1) * " ", end="")
        for j in range(2 ** i):
            idx = 2 ** i - 1 + j
            if idx >= len(A):
                print()
                break
            if j == 2 ** i - 1:
                print("{:^{width}}".format(A[idx], width=width))
            else:
                print("{:^{width}}".format(A[idx], width=width),
                      width * (2 ** (height - i + 1) - 1) * " ", sep='', end='')
    print()


def report_counts_on_basic_ops(A, loop_extracts=1, loop_inserts=1):
    original_len = len(A)
    print("\nREPORT on list of len: {}".format(original_len))
    reset_counts()
    buildHeap(A)
    print("buildHeap(A):           \t", current_counts())

    reset_counts()
    m = heapExtractMin(A)
    print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    reset_counts()
    heapInsert(A, m)
    print("heapInsert(A, {}):       \t".format(m), current_counts())

    for i in range(loop_extracts):
        reset_counts()
        m = heapExtractMin(A)
        print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    import random
    r = random.Random(0)
    for i in range(loop_inserts):
        reset_counts()
        new_number = r.randrange(0, original_len // 8)
        heapInsert(A, new_number)
        print("heapInsert(A, {}):       \t".format(new_number), current_counts())

# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

# END DO NOT MODIFY


def heapify(A, i):
    """Ensure that the tree rooted at element i in the list A is a heap,
    assuming that the trees rooted at elements left(i) and right(i) are already
    heaps. Obviously, if left(i) or right(i) are >= n, then element i simply does
    not have those out-of-bounds children. In order to implement an in-place heap sort,
    we will sometimes need to consider the tail part of A as out-of-bounds, even though
    elements do exist there. So instead of comparing with len(A), use the parameter n to
    determine if the child "exists" or not.

    Since the (up to) two child trees are already heaps, we just need to find the right
    place for the element at i. If it is smaller than both its children, then nothing
    more needs to be done, it's already a min heap. Otherwise you should swap the root
    with the smallest child and recursively heapify that tree.

    If you determine that the element at i should swap with one of its children nodes,
    MAKE SURE you do this by calling the swap function defined above.
    """

    count_heapify() # This should be the first line of the heapify function, do not change.

    if left(i) >= n and right(i) >= n:
        return
    elif left(i) < n and right(i) >= n:
        if A[i] > A[left(i)]:
            swap(A, i, left(i))
            heapify(A, left(i))
        else:
            return
    elif A[i] > A[left(i)] or A[i] > A[right(i)]:
        if A[left(i)] < A[right(i)]:
            swap(A, i, left(i))
            heapify(A, left(i))
        else:
            swap(A, i, right(i))
            heapify(A, right(i))

def buildHeap(A):
    """Turn the list A (whose elements could be in any order) into a
    heap. Call heapify on all the internal nodes, starting with
    the last internal node, and working backwards to the root.
    """

    global n
    n = len(A) # The entire list A will be turned into a heap.
    # So length of heap = length of array

    # Your code here
    middleOfList = n//2
    for i in range(middleOfList, -1, -1):
        heapify(A, i)

def heapExtractMin(A):
    """Extract the min element from the heap A. Make sure that A
    is a valid heap afterwards. Return the extracted element.
    MAKE SURE you are not extracting from an empty heap.
    This operation should perform approximately log_2(n)
    comparisons and swaps (heapify calls and swap calls).
    Your implementation should not perform O(n) (linear) work.
    Length of the array, A, should not change.
    MAKE SURE you swap elements by calling the swap function defined above.
    """


    # Your code here
    global n
    if A[0] is None:
        return
    if n < 1:
        return

    minElement = A[0]
    swap(A, 0, n-1)
    A[n-1] = None
    n-=1
    heapify(A, 0)

    return minElement

def heapInsert(A, v):
    """Insert the element v into the heap A. Make sure that A
    is a valid heap afterwards.
    This operation should perform approximately log_2(n)
    comparisons and swaps (swap calls).
    Your implementation should not perform O(n) (linear) work.
    MAKE SURE you swap elements by calling the swap function defined above.
    Always ensure n <= array_length (cannot insert when heap is full)
    """

    # Your code here
    global n

    if n >= len(A):
        return
    A[n] = v
    temp = n
    n += 1
    while A[parent(temp)] > v and parent(temp) > -1:
        swap(A, temp, parent(temp))
        temp = parent(temp)

def main():
    global db
    if len(sys.argv) > 2:
        db = True

    global n
    global array_length

    A = shuffled_list(20, 0)
    print("Complete Tree size 20:")
    printCompleteTree(A)
    buildHeap(A)
    print("Heap size 20:")
    printCompleteTree(A)

    A = shuffled_list(30, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(400, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(10000, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(100000, 0)
    report_counts_on_basic_ops(A, 3, 3)

if __name__ == "__main__":
    main()
