from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP
import time
import os
import logging
from collections import defaultdict
import socketio

# ================= SOCKET =================
sio = socketio.Client()

while True:
    try:
        sio.connect("http://localhost:5000")
        print("[+] Connected to Dashboard")
        break
    except:
        print("Retrying connection...")
        time.sleep(2)

# ================= LOGGING =================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "ids.log"),
    level=logging.INFO
)

print("[+] IDS Started...\n")

# ================= CONFIG =================
WINDOW = 10

THRESHOLDS = {
    "PORT_SCAN": 8,
    "TCP_FLOOD": 50,
    "UDP_FLOOD": 50,
    "ICMP_FLOOD": 30,
    "DNS_FLOOD": 15,
    "SSH_BRUTE": 10,
    "ARP_SPOOF": 5
}

state = defaultdict(lambda: {
    "ports": set(),
    "tcp": 0,
    "udp": 0,
    "icmp": 0,
    "dns": 0,
    "start": time.time()
})

def reset(src):
    if time.time() - state[src]["start"] > WINDOW:
        state[src] = {
            "ports": set(),
            "tcp": 0,
            "udp": 0,
            "icmp": 0,
            "dns": 0,
            "start": time.time()
        }

# ================= DETECT =================
def detect(pkt):
    if IP not in pkt:
        return None

    src = pkt[IP].src
    reset(src)

    s = state[src]

    if TCP in pkt:
        s["tcp"] += 1
        s["ports"].add(pkt[TCP].dport)

        flags = pkt[TCP].flags

        if flags == 0:
            return "NULL Scan", "No TCP flags"

    if UDP in pkt:
        s["udp"] += 1
        if pkt[UDP].dport == 53 or pkt[UDP].sport == 53:
            s["dns"] += 1

    if ICMP in pkt:
        s["icmp"] += 1

    if len(s["ports"]) > THRESHOLDS["PORT_SCAN"]:
        return "Port Scanning", "Multiple ports accessed"

    if s["tcp"] > THRESHOLDS["TCP_FLOOD"]:
        return "TCP Flood", "High TCP rate"

    if s["udp"] > THRESHOLDS["UDP_FLOOD"]:
        return "UDP Flood", "High UDP rate"

    if s["icmp"] > THRESHOLDS["ICMP_FLOOD"]:
        return "ICMP Flood", "High ICMP rate"

    if s["dns"] > THRESHOLDS["DNS_FLOOD"]:
        return "DNS Flood", "High DNS traffic"

    return None

# ================= PROCESS =================
def process(pkt):
    if IP not in pkt:
        return

    src = pkt[IP].src
    attack = detect(pkt)

    if attack:
        name, reason = attack

        print(f"[ATTACK] {name} from {src}")

        sio.emit("attack_event", {
            "timestamp": time.strftime("%H:%M:%S"),
            "src": src,
            "attack": name,
            "reason": reason,
            "time": "1s"
        })

    else:
        sio.emit("attack_event", {
            "timestamp": time.strftime("%H:%M:%S"),
            "src": src,
            "attack": "Normal",
            "reason": "Normal traffic",
            "time": "0s"
        })

# ================= START =================
sniff(iface="eth1", prn=process, store=False)
