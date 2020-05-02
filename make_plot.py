import numpy as np
from matplotlib import pyplot as plt
import sys


def read_file(filename):
    """This function reads the numbers from a .csv file."""
    data = np.genfromtxt(filename, delimiter=',')
    return data[:, 0], data[:, 1]


def make_plot(x, y, name, log_x=False, log_y=False):
    """This function makes a plot from a 2d array. Using the log_x
    and log_y flags, each of the axis can be drawn in log scale"""
    if log_x:
        x = np.log2(x)
    if log_y:
        y = np.log2(y)
    plt.plot(x, y, label=name)


if __name__ == "__main__":

    filename = sys.argv[1]
    x, y = read_file(filename)
    flag_log_x = int(sys.argv[2])
    flag_log_y = int(sys.argv[3])

    make_plot(x, y, filename, log_x=flag_log_x, log_y=flag_log_y)

    x_label = 'x'
    if flag_log_x:
        x_label = 'log x'
    y_label = 'y'
    if flag_log_y:
        y_label = 'log y'

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig('plots_' + filename.split('.')[0] + '_' + str(flag_log_x) + '_' + str(flag_log_y))
    plt.show()
