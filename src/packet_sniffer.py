import pyshark

def capture_packets(interface="eth0"):
    """Capture network packets on a specified interface."""
    print(f"Starting packet capture on {interface}...")
    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously():
        try:
            print(f"Packet: {packet}")
            yield {
                "source": packet.ip.src,
                "destination": packet.ip.dst,
                "protocol": packet.highest_layer,
                "length": packet.length,
            }
        except AttributeError:
            continue
