from scapy.all import sniff

def handle(pkt):
    if pkt.haslayer("IP"):
        print(pkt.summary())

sniff(iface="eth0", prn=handle, store=False)
