import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Initialize the neural network parameters and architecture
        self.layers = []
        self.learning_rate = 0.001
        self.weights = []
        self.biases = []

    def add_layer(self, num_neurons, activation_func):
        # Add a new layer to the neural network with specified number of neurons and activation function
        self.layers.append((num_neurons, activation_func))

    def initialize_weights(self):
        # Initialize the weights and biases for all layers
        for i in range(1, len(self.layers)):
            prev_neurons, _ = self.layers[i-1]
            curr_neurons, _ = self.layers[i]
            weights = np.random.randn(curr_neurons, prev_neurons)
            biases = np.zeros((curr_neurons, 1))
            self.weights.append(weights)
            self.biases.append(biases)

    def forward_propagation(self, inputs):
        # Perform forward propagation through the neural network
        activations = [inputs]
        for i in range(len(self.layers)):
            neurons, activation_func = self.layers[i]
            weights = self.weights[i]
            biases = self.biases[i]
            z = np.dot(weights, activations[-1]) + biases
            a = activation_func(z)
            activations.append(a)
        return activations

    def backward_propagation(self, inputs, targets):
        # Perform backward propagation and update the weights and biases using gradient descent
        activations = self.forward_propagation(inputs)
        delta = activations[-1] - targets
        for i in range(len(self.layers)-1, 0, -1):
            a = activations[i]
            a_prev = activations[i-1]
            delta = np.dot(self.weights[i].T, delta) * a * (1 - a)
            grad_weights = np.dot(delta, a_prev.T)
            grad_biases = np.sum(delta, axis=1, keepdims=True)
            self.weights[i] -= self.learning_rate * grad_weights
            self.biases[i] -= self.learning_rate * grad_biases

    def train(self, training_data, epochs):
        # Train the neural network using the provided training data
        for epoch in range(epochs):
            for inputs, targets in training_data:
                self.backward_propagation(inputs, targets)

    def predict(self, inputs):
        # Use the trained neural network to make predictions
        activations = self.forward_propagation(inputs)
        return activations[-1]
