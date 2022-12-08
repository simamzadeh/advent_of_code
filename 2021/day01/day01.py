# PART 1
import numpy as np


def read_data():
    # open and read file with list of depths
    depths_input = open("input.txt").read()
    depths_str_list = depths_input.split("\n")[:-1]
    depths_int_list = []
    for i in depths_str_list:
        depths_int_list.append(int(i))
    return depths_int_list


def depth_diff(list):
    # find list of differences
    diffs = np.diff(list)

    # if difference is greater than zero add to count
    count = 0
    for i in diffs:
        if i > 0:
            count = count + 1
    return count


print(depth_diff(read_data()))

