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
    if len(in_list) <= 1:
        return 0
    if len(in_list) % 2 != 0:
        temp = (len(in_list) // 2) + 1
    else:
        temp = (len(in_list) // 2)

    list_a = in_list[0: temp]
    list_b = in_list[temp:]

    ra = count_inversions(list_a)
    rb = count_inversions(list_b)

    count = merge_i(list_a, list_b)

    return ra + rb + count


# implement
def merge_i(l_list, r_list):
    count = 0
    i = 0
    j = 0
    result = []
    while i < len(l_list) and j < len(r_list):
        if l_list[i] < r_list[j]:
            result.append(l_list[i])
            i += 1
        if l_list[i] > r_list[j]:
            result.append(r_list[j])
            count += (len(l_list) - i)
            j += 1

    if len(l_list) < 1 and len(r_list) > 0:
        result.append(r_list)
    if len(r_list) < 1 and len(l_list) > 0:
        result.append(l_list)
    return count


# provided
if __name__ == '__main__':
    filename = sys.argv[1]
    in_list = read_array(filename)
    print(count_inversions(in_list))
