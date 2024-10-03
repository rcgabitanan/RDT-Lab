import random

class Receiver:
    def __init__(self):
        self.expected_seq = 0

    def acknowledge(self, packet):
        """Acknowledge or reject the packet."""
        if packet.corrupt_prob > 60:  # Simulate packet corruption
            print(f"[Receiver] Packet corrupted: Packet(seq={packet.seq_num})")
            return "NACK"
        elif packet.seq_num != self.expected_seq:
            print(f"[Receiver] Out of sequence: Expected {self.expected_seq}, got {packet.seq_num}")
            return "NACK"
        else:
            print(f"[Receiver] Received expected packet: Packet(seq={packet.seq_num})")
            self.expected_seq = 1 if self.expected_seq == 0 else 0
            return "ACK"
