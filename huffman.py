import sys
import math
import datetime


class Heap:
    def __init__(self, A):
        self.A = A
        self.length = len(A)
        self.n = self.length

    def swap(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return self.left(i) + 1

    def heapify(self, i):
        if self.left(i) >= self.n and self.right(i) >= self.n:
            return
        elif self.left(i) < self.n <= self.right(i):

            if self.A[i] == self.A[self.left(i)] or self.A[i] < self.A[self.left(i)]:

                self.swap(i, self.left(i))
                self.heapify(self.left(i))
            else:
                return
        else:
            if self.A[self.left(i)] < self.A[self.right(i)]:
                self.swap(i, self.left(i))
                self.heapify(self.left(i))
            else:
                self.swap(i, self.right(i))
                self.heapify(self.right(i))

    def buildHeap(self):
        middleOfList = self.n // 2
        for i in range(middleOfList, -1, -1):
            self.heapify(i)

    def heapExtractMin(self):
        if self.A[0] is None:
            return
        if self.n < 1:
            return

        minElement = self.A[0]
        self.swap(0, self.n - 1)
        self.A[self.n - 1] = None
        self.n -= 1

        self.heapify(0)

        return minElement

    def heapInsert(self, v):

        if self.n >= self.length:
            return
        self.A[self.n] = v
        temp = self.n
        self.n += 1

        if (self.A[self.parent(temp)]) is not None:
            while (self.A[self.parent(temp)] < v and self.parent(temp) > 0):
                print(self.A[self.parent(temp)])
                self.swap(temp, self.parent(temp))
                temp = self.parent(temp)
                if self.A[self.parent(temp)] is None:
                    break



def file_character_frequencies(file_name):
    freqs = {}
    numOfChars = 0
    with open(file_name) as file:
        for line in file:
            fields = line.split()
            for word in fields:
                for letter in word:
                    if letter in freqs:
                        freqs[letter] += 1
                    else:
                        freqs[letter] = 1
                    numOfChars += 1
    for key in freqs:
        freqs[key] /= numOfChars
    return freqs


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]


def huffman_codes_from_frequencies(frequencies):
    # Suggested helper
    huffmanArray = []
    for key in frequencies:
        temp = PriorityTuple((frequencies[key], key))
        huffmanArray.append(temp)
    priorityQueue = Heap(huffmanArray)
    priorityQueue.buildHeap()
    while priorityQueue.n > 1:
        temp1 = priorityQueue.heapExtractMin()
        if temp1 is None:
            break
        temp2 = priorityQueue.heapExtractMin()
        if temp2 is None:

            break
        newNode = PriorityTuple((temp1[0] + temp2[0], (temp1, temp2)))

        priorityQueue.heapInsert(newNode)
    print(priorityQueue.A)




def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
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

def shuffled_list(length, seed):
    lst = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(lst)
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



def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    codes = huffman_codes_from_frequencies(frequencies)
    """
    l = shuffled_list(20, 0)
    h = Heap(l)
    print(l)
    printCompleteTree(h.A)
    h.buildHeap()
    printCompleteTree(h.A)
    """




if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
