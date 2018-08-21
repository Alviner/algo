# -*- coding: utf-8 -*-

import glob
import os

dataset_dir = os.path.join(os.getcwd(), 'dataset')

class_map = {
    'a': 1,
    'other': 0
}

class_files = {
    'a': [],
    'other': []
}


class Neuron:
    def __init__(self, n: int, m: int, threshold=35):
        self.weight = [[0 for i in range(n)] for j in range(m)]
        self.threshold = threshold

    def _in(self, filename: str):
        input = []
        res = 0
        with open(filename, 'r') as in_file:
            for line in in_file.readlines():
                row = []
                for char in line:
                    if char != '\n':
                        row.append(int(char))
                input.append(row)
        assert len(input) == len(self.weight)
        assert len(input[0]) == len(self.weight[0])

        for j in range(len(input)):
            for i in range(len(input[0])):
                res += input[i][j] * self.weight[i][j]
        return 1 if res > self.threshold else 0


def test_neuron():
    neuron = Neuron(10, 10)
    for name, _ in class_files.items():
        class_files[name] = glob.glob(os.path.join(dataset_dir, name, '*.txt'))
        for file in class_files[name]:
            assert neuron._in(file) == 0


if __name__ == '__main__':
    test_neuron()