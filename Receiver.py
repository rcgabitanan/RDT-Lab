import random

class Receiver:
    def __init__(self):
        self.expected_seq = 0

    def acknowledge(self, packet):
        """Acknowledge or reject the packet."""
        ack = Ack(packet.seq_num)
        if packet.corrupt_prob < 60:  # Simulate packet corruption
            print(f"[Receiver] Packet corrupted: Packet(seq={packet.seq_num})")
            ack.code = "NACK"
        elif packet.seq_num != self.expected_seq:
            print(f"[Receiver] Out of sequence: Expected {self.expected_seq}, got {packet.seq_num}")
            ack.code = "NACK"
        else:
            print(f"[Receiver] Received expected packet: Packet(seq={packet.seq_num}). Sending ACK.")
            self.expected_seq = 1 if self.expected_seq == 0 else 0
            ack.code = "ACK"
            
        return ack

class Ack:
    code = ""
    seq_num = 0
    
    def __init__(self, seq_num):
        self.seq_num = seq_num