import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        
        self.bias1 = np.zeros((1, self.hidden_size))
        self.bias2 = np.zeros((1, self.output_size))
        
    def forward(self, X):
        self.hidden_layer = np.dot(X, self.weights1) + self.bias1
        self.hidden_layer_activation = self.sigmoid(self.hidden_layer)
        
        self.output_layer = np.dot(self.hidden_layer_activation, self.weights2) + self.bias2
        self.output_layer_activation = self.sigmoid(self.output_layer)
        
        return self.output_layer_activation
    
    def backward(self, X, y, output, learning_rate):
        self.error = y - output
        
        self.output_delta = self.error * self.sigmoid_derivative(output)
        self.hidden_error = np.dot(self.output_delta, self.weights2.T)
        
        self.hidden_delta = self.hidden_error * self.sigmoid_derivative(self.hidden_layer_activation)
        
        self.weights2 += learning_rate * np.dot(self.hidden_layer_activation.T, self.output_delta)
        self.weights1 += learning_rate * np.dot(X.T, self.hidden_delta)
        
        self.bias2 += learning_rate * np.sum(self.output_delta, axis=0)
        self.bias1 += learning_rate * np.sum(self.hidden_delta, axis=0)
        
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
    
    def predict(self, X):
        return self.forward(X)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
