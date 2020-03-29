import sys

array_length = 0 # ONCE SET FOR A GIVEN ARRAY, THIS SHOULD NEVER CHANGE
# EVEN WHEN DOING OPERATIONS LIKE EXTRACT-MIN AND HEAP-INSERT

n = 0 #length of the 'heap'. n <= array_length

swap_count = 0
heapify_call_count = 0


class Node:
    def __init__(self):
        self.left = None
        self.right = None


def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0


def count_heapify():
    global heapify_call_count
    heapify_call_count += 1


def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1


def heapify(A, i):
    count_heapify()
    if left(i) >= n and right(i) >= n:
        return
    elif left(i) < n <= right(i):
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
    global n
    n = len(A)  # The entire list A will be turned into a heap.
    middleOfList = (n // 2)
    for i in range(middleOfList, -1, -1):
        heapify(A, i)


def heapExtractMin(A):
    global n
    if A[0] is None:
        return
    if n < 1:
        return
    minElement = A[0]
    swap(A, 0, n - 1)
    A[n - 1] = None
    n -= 1
    heapify(A, 0)
    return minElement


def heapInsert(A, v):
    global n
    if n >= len(A):
        return
    A[n] = v
    temp = n
    n += 1
    if (A[parent(temp)]) is not None:
        while A[parent(temp)] > v and parent(temp) >= 0:
            swap(A, temp, parent(temp))
            temp = parent(temp)
            if A[parent(temp)] is None:
                break


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """

    def __lt__(self, other):

        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):

        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x


def left(i):
    return (2 * i) + 1


def right(i):
    return left(i) + 1


def buildCodes(abc, freqs, total=""):
    a = str(abc)
    value = 0
    for char in a.split():
        if char in freqs:
            freqs[char] = "{0:b}".format(value)
            value += 1


def file_character_frequencies(file_name):
    freqs = {" ": 0, "\n": 0}
    numOfChars = 0
    with open(file_name) as file:
        for line in file:
            fields = line.split()
            nl = line.split('\n')
            for word in fields:
                for letter in word:
                    if letter in freqs:
                        freqs[letter] += 1
                    else:
                        freqs[letter] = 1
                    numOfChars += 1
        if len(nl) > 1:
            freqs["\n"] += 1
            numOfChars += 1
        freqs[" "] += len(fields) - 1
        numOfChars += len(fields) - 1
    for key in freqs:
        freqs[key] /= numOfChars
    return freqs


def huffman_codes_from_frequencies(frequencies):
    global n
    huffmanArray = []
    for key in frequencies:
        temp = PriorityTuple((frequencies[key], key))
        huffmanArray.append(temp)
    buildHeap(huffmanArray)
    while n != 1:
        temp1 = heapExtractMin(huffmanArray)
        temp2 = heapExtractMin(huffmanArray)
        node = Node()
        node.left = temp1
        node.right = temp2
        temp3 = temp1[0] + temp2[0]
        temp4 = PriorityTuple((temp3, node))
        heapInsert(huffmanArray, temp4)

    for key in frequencies:
        frequencies[key] = ""

    foo(huffmanArray[0], frequencies, prefix="")
    return frequencies


def foo(a, freqs, prefix):
    if a[1] not in freqs:
        foo(a[1].left, freqs, prefix + "0")
        foo(a[1].right, freqs, prefix + "1")
    else:
        freqs[a[1]] += prefix


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
