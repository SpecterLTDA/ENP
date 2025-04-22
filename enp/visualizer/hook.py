import matplotlib.pyplot as plt

def plot_spike_activity(outputs):
    plt.figure(figsize=(10, 1))
    plt.imshow([outputs], cmap='binary', aspect='auto')
    plt.title("Neuron Spikes")
    plt.xlabel("Neuron Index")
    plt.yticks([])
    plt.show()