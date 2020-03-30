import sys


# provided
def read_array(filename):
    in_list = []
    with open(filename, 'r+') as input_file:
        for line in input_file:
            in_list.append(int(line))
    return in_list


def merge_sort(in_list, l_index, r_index):
    if l_index >= r_index:
        return 0
    mid = (l_index + r_index) // 2
    a = merge_sort(in_list, l_index, mid)
    b = merge_sort(in_list, mid + 1, r_index)
    c = merge_i(in_list, l_index, r_index, mid)
    return a + b + c[0]


def count_inversions(in_list):
    if len(in_list) <= 1:
        return 0
    return merge_sort(in_list, 0, len(in_list) - 1)


def merge_i(in_list, l_index, r_index, mid):
    l_list = in_list[l_index:mid + 1]
    r_list = in_list[mid + 1:r_index + 1]
    l_index_copy = 0
    r_index_copy = 0
    sorted_index = l_index
    result = 0

    while l_index_copy < len(l_list) and r_index_copy < len(r_list):
        if l_list[l_index_copy] <= r_list[r_index_copy]:
            in_list[sorted_index] = l_list[l_index_copy]
            l_index_copy += 1
        else:
            in_list[sorted_index] = r_list[r_index_copy]
            result += (len(l_list) - l_index_copy)
            r_index_copy += 1
        sorted_index += 1
    while l_index_copy < len(l_list):
        in_list[sorted_index] = l_list[l_index_copy]
        l_index_copy += 1
        sorted_index += 1

    while r_index_copy < len(r_list):
        in_list[sorted_index] = r_list[r_index_copy]
        r_index_copy += 1
        sorted_index += 1
    return result, in_list


if __name__ == '__main__':
    filename = sys.argv[1]
    in_list = read_array(filename)
    print(count_inversions(in_list))
