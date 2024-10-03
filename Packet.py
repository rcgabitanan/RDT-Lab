import random

class Packet:
    seq_num = 0
    data = ""
    loss_prob = 0
    corrupt_prob = 0
    
    def __init__(self, seq_num, data):
        self.seq_num = seq_num
        self.data = data
        self.reset_probabilities()

    def reset_probabilities(self):
        """Resets the packet's loss and corruption probabilities."""
        self.loss_prob = self.generate_probability()
        self.corrupt_prob = self.generate_probability()

    def generate_probability(self):
        """Generates a random probability."""
        return random.randint(2, 99)
