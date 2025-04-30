from .neuron import ENPNeuron

class ENPNetwork:
    def __init__(self, topology):
        self.neurons = {nid: ENPNeuron(nid) for nid in topology["neurons"]}
        self.connections = topology["connections"]  # Ex: {("A", "B"): 0.3}

    def step(self, inputs):
        spikes = {}
        for nid, current in inputs.items():
            spike = self.neurons[nid].integrate(current)
            spikes[nid] = spike

        outputs = {}
        for (src, tgt), weight in self.connections.items():
            if spikes.get(src):
                outputs[tgt] = outputs.get(tgt, 0.0) + weight

        return outputs