import numpy as np

class NN(object):
    def __init__(self, W1, W2, l):
        self.W1 = W1
        self.W2 = W2
        self.u1 = 0
        self.z1 = 0
        self.u2 = 0
        self.output = 0
        self.l = l

    def update(self, y):
        w1_grad, w2_grad = self._backward(y)
        self.W1 -= self.l * w1_grad
        self.W2 -= self.l * w2_grad.T
        print('W1', self.W1)
        print('W2', self.W2)

    def forward(self, X):
        self.input = X
        self.u1 = self.W1 @ X
        self.z1 = np.tanh(self.u1)
        self.u2 = (self.W2 @ self.z1)[0,0]
        self.output = np.tanh(self.u2)

        return self.output

    def _backward(self, y):
        delta_2 = (self.output - y) * (1 - self.u2 * self.u2)
        w2_grad = delta_2 * self.z1

        delta_1 = delta_2 * self.W2.T * (np.ones((2,1)) - self.u1 * self.u1)
        w1_grad = np.tile(self.input.T, (2,1)) * np.tile(delta_1, (1,2))

        print(w1_grad)
        print(w2_grad)

        return w1_grad, w2_grad


STUDENT_ID = input("please, input a your id:")
print("Your ID is {}".format(STUDENT_ID))

b_3, b_2, b_1 = [int(sid) for sid in STUDENT_ID[-3:]]
print("b_1 = {}, b_2 = {}, b_3 = {}".format(b_1, b_2, b_3))

w1 = np.zeros((2,2))
w2 = np.zeros((1,2))
w1[0,0] = - (b_2 + 1) / 10
w1[1,0] = - (b_3 + 1) / 10
w1[0,1] = (b_1 + 1) / 10
w1[1,1] = (b_3 + 1) / 10
w2[0,0] = (b_1 + 1) / 10
w2[0,1] = - (b_2 + 1) / 10 
print(w1, w2)

model = NN(w1, w2, 1)
print(model.forward(np.array([[1], [1]])))
model.update(1)
print(model.forward(np.array([[0], [1]])))
model.update(-1)
print(model.forward(np.array([[0], [0]])))
model.update(1)
print(model.forward(np.array([[1], [0]])))
model.update(-1)
