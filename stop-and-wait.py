import sender

def stop_and_wait():
    """Run the Stop-and-Wait protocol."""
    print("=== Starting Stop-and-Wait Protocol ===")
    sender_instance = sender.Sender()  # Reuse the sender logic
    
    # Once all packets are sent, terminate the connection
    print("=== All packets sent. Terminating connection ===")

if __name__ == "__main__":
    stop_and_wait()
