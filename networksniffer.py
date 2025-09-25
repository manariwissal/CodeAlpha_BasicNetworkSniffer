from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# Fonction pour analyser chaque paquet
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")
        
        # Si c'est TCP ou UDP, afficher les ports
        if TCP in packet:
            print(f"TCP Source Port: {packet[TCP].sport} -> Dest Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Source Port: {packet[UDP].sport} -> Dest Port: {packet[UDP].dport}")
        
        # Afficher le payload si présent
        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload}\n")

# Capture des paquets en temps réel
print("Sniffing en cours... (CTRL+C pour arrêter)")
sniff(
    iface="Intel(R) Dual Band Wireless-AC 8260",  # Ton interface Wi-Fi active
    prn=packet_callback,
    store=False
)
