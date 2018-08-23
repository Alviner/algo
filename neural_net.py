# -*- coding: utf-8 -*-

import glob
import os


class Neuron:
    dataset_dir = os.path.join(os.getcwd(), 'dataset')

    class_map = {
        'a': 1,
        'other': 0
    }

    class_files = {
        'a': [],
        'other': []
    }

    def __init__(self, n: int, m: int, threshold=35):
        self.weight = [[0 for i in range(n)] for j in range(m)]
        self.threshold = threshold

    def get_data(self, filename: str):
        input = []
        with open(filename, 'r') as in_file:
            for line in in_file.readlines():
                row = []
                for char in line:
                    if char != '\n':
                        row.append(int(char))
                input.append(row)
        assert len(input) == len(self.weight)
        assert len(input[0]) == len(self.weight[0])
        return input

    def predict(self, in_data):
        res = 0
        for j in range(len(in_data)):
            for i in range(len(in_data[0])):
                res += in_data[i][j] * self.weight[i][j]
        return 1 if res > self.threshold else 0

    def up(self, in_data):
        for j in range(len(self.weight)):
            for i in range(len(self.weight[j])):
                self.weight[i][j] += in_data[i][j]

    def down(self, in_data):
        for j in range(len(self.weight)):
            for i in range(len(self.weight[j])):
                self.weight[i][j] -= in_data[i][j]

    def train(self):
        go_on = True

        while go_on:
            error = False
            for name, _ in Neuron.class_files.items():
                Neuron.class_files[name] = glob.glob(os.path.join(Neuron.dataset_dir, name, '*.txt'))
                for file in Neuron.class_files[name]:
                    in_value = self.get_data(file)
                    if self.predict(in_value) == 0 and name == 'a':
                        error = True
                        self.up(in_value)
                    elif self.predict(in_value) == 1 and name == 'other':
                        error = True
                        self.down(in_value)
            if not error:
                go_on = False

    def test(self):
        results = []
        for name, _ in Neuron.class_files.items():
            Neuron.class_files[name] = glob.glob(os.path.join(Neuron.dataset_dir, name, '*.txt'))
            for file in Neuron.class_files[name]:
                in_value = self.get_data(file)
                res = "a" if self.predict(in_value) == 1 else "other"
                results.append((name, res))
        return results


def test_predict():
    neuron = Neuron(10, 10)
    for name, _ in Neuron.class_files.items():
        Neuron.class_files[name] = glob.glob(os.path.join(Neuron.dataset_dir, name, '*.txt'))
        for file in Neuron.class_files[name]:
            assert neuron.predict(neuron.get_data(file)) == 0


def test_train():
    neuron = Neuron(10, 10)
    neuron.train()
    results = neuron.test()

    for (expext, result) in results:
        assert expext == result


if __name__ == '__main__':
    test_predict()
    test_train()
