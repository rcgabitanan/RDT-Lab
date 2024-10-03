import Receiver
import Packet
import time

class Sender:
    timeout = 2  # 2 seconds timeout
    receiver = Receiver.Receiver()
    seq = 0  # Initial sequence number

    def __init__(self):
        print("[Sender] Initialized")
        self.packets = self.generate_packets()
        self.send_packets(self.packets)

    def generate_packets(self):
        """Generates 10 packets."""
        packets = []
        for i in range(10):
            packets.append(Packet.Packet(self.seq, f"Message {i}"))
            self.seq = 1 if self.seq == 0 else 0  # Toggle sequence
        return packets

    def send_packets(self, packets):
        """Sends packets using Stop-and-Wait protocol."""
        for packet in packets:
            self.send_packet(packet)

    def send_packet(self, packet):
        """Handles sending a single packet, waiting for ACK or retransmission."""
        while True:
            print(f"[Sender][Stop-and-Wait] Sending: Packet(seq={packet.seq_num}, data={packet.data})")
            ack = self.receiver.acknowledge(packet)
            if ack == "ACK":
                print(f"[Sender] Received ACK: {ack} for Packet(seq={packet.seq_num})")
                break
            else:
                print(f"[Sender] Received NACK or no ACK. Retransmitting: Packet(seq={packet.seq_num})")
                packet.reset_probabilities()  # Reset probabilities to simulate new conditions
                time.sleep(self.timeout)  # Simulate the timeout before retransmission

if __name__ == "__main__":
    sender = Sender()
