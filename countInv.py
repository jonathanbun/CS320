import sys

# provided
def read_array(filename):
    in_list = []
    with open(filename, 'r+') as input_file:
        for line in input_file:
            in_list.append(int(line))
    return in_list


# implement
def count_inversions(in_list):
    return 0

# implement
def merge_i(l_list, r_list, in_list):
    pass

# provided
if __name__ == '__main__':
    filename = sys.argv[1]
    in_list = read_array(filename)
    print(count_inversions(in_list))