from enp.core.neuron import ENPNeuron

def test_neuron_fire():
    neuron = ENPNeuron(neuron_id=1, threshold=0.5)
    spike = neuron.integrate(0.6)
    assert spike is True
