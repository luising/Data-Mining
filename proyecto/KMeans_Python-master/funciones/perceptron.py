import random
import numpy as np


class Perceptron:

    def __init__(self, input_number, step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size

    def predict(self, inputs="no"):
        pesos = []
        if inputs == "no":
            for a in range(13):
                con = np.zeros(13)
                con[a] = 1
                weighted_average = sum(w * elm for w, elm in zip(self._w, con))
                pesos.append(weighted_average)
        else:
            for a in range(13):
                weighted_average = sum(w * elm for w, elm in zip(self._w, inputs))
                pesos.append(weighted_average)

    def train(self, inputs, ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w + self._eta * error * x for w, x in zip(self._w, inputs)]
        return error
