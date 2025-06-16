from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"\n[+] Packet: {ip_src} → {ip_dst} | Protocol: {proto}")

        if Raw in packet:
            payload = packet[Raw].load
            print("    Payload:", payload[:50])  # Show first 50 bytes

def main():
    print("=== Packet Sniffer is running... Press Ctrl+C to stop ===")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
