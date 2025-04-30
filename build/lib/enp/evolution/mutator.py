import random

def mutate_network(network, mutation_rate=0.1, mutation_strength=0.05):
    for neuron in network.neurons:
        if random.random() < mutation_rate:
            neuron.threshold += random.uniform(-mutation_strength, mutation_strength)
            neuron.decay += random.uniform(-mutation_strength, mutation_strength)
            neuron.threshold = max(0.1, min(neuron.threshold, 10.0))
            neuron.decay = max(0.1, min(neuron.decay, 0.99))