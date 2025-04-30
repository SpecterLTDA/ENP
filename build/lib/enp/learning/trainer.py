class Trainer:
    def __init__(self, network, memory, reward_function):
        self.network = network
        self.memory = memory
        self.reward_function = reward_function

    def train_step(self, input_vector):
        outputs = self.network.forward(input_vector)
        reward = self.reward_function(outputs)
        trace = {"inputs": input_vector, "outputs": outputs, "reward": reward}
        self.memory.store(trace)
        return reward