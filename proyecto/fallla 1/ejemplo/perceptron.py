import random


class Perceptron:

    def __init__(self, input_number, step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size

    def predict(self, inputs):
        return sum(w * elm for w, elm in zip(self._w, inputs))

    def train(self, inputs, ex_output):
        output = self.predict(inputs)
        print("salidad ", output)
        error = ex_output - output
        if error != 0:
            self._w = [w + self._eta * error * x for w, x in zip(self._w, inputs)]
        return error
