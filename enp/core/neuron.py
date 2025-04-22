import numpy as np

class ENPNeuron:
    def __init__(self, neuron_id, threshold=1.0, decay=0.95):
        self.id = neuron_id
        self.membrane_potential = 0.0
        self.threshold = threshold
        self.decay = decay
        self.spike = False
        self.trace = 0.0  # memória curta

    def integrate(self, input_current):
        self.membrane_potential *= self.decay
        self.membrane_potential += input_current
        self.spike = self.membrane_potential >= self.threshold

        if self.spike:
            self.membrane_potential = 0.0
            self.trace += 1
        else:
            self.trace *= self.decay

        return self.spike