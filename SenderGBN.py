from ReceiverGBN import ReceiverGBN
import Packet
import time

class SenderGBN:
    window_size = 4
    timeout = 2  # Timeout in seconds
    receiver = ReceiverGBN()
    base = 0  # First sequence number of the window
    next_seq_num = 0  # Next sequence number to send
    total_packets = 10  # Total packets to send

    def __init__(self):
        print("[Sender][GBN] Initialized")
        self.packets = self.generate_packets()
        self.send_window()

    def generate_packets(self):
        """Generates packets to be sent in Go-Back-N protocol."""
        packets = []
        for i in range(self.total_packets):
            packets.append(Packet.Packet(i, f"Message {i}"))
        return packets

    def send_window(self):
        """Send all packets in the current window."""
        while self.base < self.total_packets:
            # Send packets within the window
            while self.next_seq_num < self.base + self.window_size and self.next_seq_num < self.total_packets:
                self.send_packet(self.packets[self.next_seq_num])
                self.next_seq_num += 1

            # Wait for ACK
            self.wait_for_ack()

    def send_packet(self, packet):
        """Simulate sending a packet."""
        if packet.loss_prob > 60:
            print(f"[Sender][GBN] Packet Lost: Packet(seq={packet.seq_num}, data={packet.data})")
        else:
            print(f"[Sender][GBN] Sending: Packet(seq={packet.seq_num}, data={packet.data})")

    def wait_for_ack(self):
        """Wait for ACK or timeout."""
        time.sleep(self.timeout)  # Simulate waiting for ACK with a timeout
        for i in range(self.base, self.next_seq_num):
            ack = self.receiver.acknowledge(self.packets[i])
            if ack.startswith("ACK"):
                ack_num = int(ack[3:])
                print(f"[Sender][GBN] Received {ack}")
                self.base = ack_num + 1  # Slide the window forward
            else:
                print(f"[Sender][GBN] NACK received or timeout. Resending from Packet(seq={self.base})")
                self.next_seq_num = self.base  # Retransmit from base
                break  # Break and retransmit the window

if __name__ == "__main__":
    sender_gbn = SenderGBN()
