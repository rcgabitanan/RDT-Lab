from SenderGBN import SenderGBN

def go_back_n():
    """Run the Go-Back-N protocol."""
    print("=== Starting Go-Back-N Protocol ===")
    sender_instance = SenderGBN()  # Reuse the sender logic
    
    print("=== All packets sent using Go-Back-N Protocol ===")

if __name__ == "__main__":
    go_back_n()
