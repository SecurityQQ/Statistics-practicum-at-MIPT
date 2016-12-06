import numpy as np

names, marks = [], []
with open('marks.csv') as f:
    for line in f:
        split_line = list(map(lambda x: '0' if x == '' else x, line[:-1].split(',')))
        names.append(split_line[0])
        marks.append(list(map(int, split_line[1:])))

marks = np.array(marks)
