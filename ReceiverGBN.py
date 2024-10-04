import random

class ReceiverGBN:
    def __init__(self):
        self.expected_seq = 0

    def acknowledge(self, packet):
        """Acknowledge only the last correctly received in-order packet."""
        if packet.corrupt_prob > 60:  # Simulate packet corruption
            print(f"[Receiver][GBN] Packet corrupted: Packet(seq={packet.seq_num})")
            return "NACK"
        elif packet.seq_num != self.expected_seq:
            print(f"[Receiver][GBN] Out of sequence: Expected {self.expected_seq}, got {packet.seq_num}")
            return f"ACK{self.expected_seq - 1}"  # Acknowledge the last correctly received packet
        else:
            print(f"[Receiver][GBN] Received expected packet: Packet(seq={packet.seq_num})")
            self.expected_seq += 1  # Move the expected sequence forward
            return f"ACK{packet.seq_num}"
