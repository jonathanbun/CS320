import numpy as np


def write_output(filename, answer):
    '''answer is an array of 2 ints for the two closest points'''
    with open('output_' + filename, 'w') as file:
        file.write(str(answer[0]) + ' ' + str(answer[1]))


def get_closest_pair(P):
    '''Wrapper function. Creates sorted X and Y arrays from P and makes the initial
    call to compute_closest_points(P, X, Y)
    This function will be called and timed by the grading script'''
    # Your code here
    temp = P.copy()
    X = sorted(temp, key=lambda row: row[1])
    Y = sorted(temp, key=lambda row: row[2])
    print(X)
    print(Y)
    print(P)

    point1, point2, delta = compute_closest_points(P, X, Y)
    return point1, point2, delta


def compute_closest_points(P, X, Y):
    '''Takes P (original array), X (array sorted by x coordinates), Y (array sorted
    by y coordinates) as input and returns the pair of closest points, along
    with the distance between them
    Implement Divide and Conquer strategy here'''

    return 0,0,0


def brute_force(X):
    '''Implements brute force method to determine closest pair when X has <=3
    points'''
    # Your code here
    # return point1, point2, delta


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    P = np.genfromtxt(filename)

    import time
    start_time = time.process_time()
    pt1, pt2, delta = get_closest_pair(P)
    end_time = time.process_time()

    print("time taken: {}".format(end_time - start_time))
    write_output(filename, [int(pt1), int(pt2)])