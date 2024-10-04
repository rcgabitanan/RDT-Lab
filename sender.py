import Receiver
import Packet
import time

class Sender:
    timeout = 2  # 2 seconds timeout
    receiver = Receiver.Receiver()
    seq = 0  # Initial sequence number

    def __init__(self):
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
            start_time = time.time()  # Start the timer
            print(f"[Sender][Stop-and-Wait] Sending: Packet(seq={packet.seq_num}, data={packet.data})")

            # Simulate packet loss with a delay if loss_prob is odd
            if packet.loss_prob > 60:  # Check if loss_prob is odd
                print(f"[Network] Packet loss. Retransmitting: Packet(seq={packet.seq_num}, data={packet.data})")
                time.sleep(3)  # Add a 3-second delay to simulate packet loss
                
            else:
                ack = None
                while time.time() - start_time < self.timeout:
                    ack = self.receiver.acknowledge(packet)

                    if ack.code == "ACK":
                        print(f"[Sender] Received ACK: ACK({ack.code}). Moving to the next packet.)")
                        return  # Exit the loop and move to the next packet
                    elif ack.code == "NACK":
                        print(f"[Sender] Received NACK. Retransmitting: Packet(seq={packet.seq_num})")
                        break  # Break and retransmit the packet

            # If no ACK received within timeout, retransmit the packet
            if time.time() - start_time >= self.timeout:
                print(f"[Sender][Stop-and-Wait] Timeout waiting for ACK. Retransmitting: Packet(seq={packet.seq_num}, data={packet.data})")
                packet.reset_probabilities()  # Reset loss/corruption probabilities
                continue  # Continue the loop to retransmit the packet
            
            print(f"[Sender][Stop-and-Wait] Sending: Packet(seq={packet.seq_num}, data={packet.data})")
            ack = self.receiver.acknowledge(packet)
            if ack.code == "ACK":
                print(f"[Sender] Received ACK: ACK({ack.seq_num}). Moving to next packet.")
                break
            else:
                print(f"[Sender] Received NACK or no ACK. Retransmitting: Packet(seq={packet.seq_num})")
                packet.reset_probabilities()  # Reset probabilities to simulate new conditions
                time.sleep(self.timeout)  # Simulate the timeout before retransmission

if __name__ == "__main__":
    sender = Sender()


