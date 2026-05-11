import pandas as pd

features = []

def extract(pkt):
    if pkt.haslayer("IP"):
        features.append([
            pkt["IP"].len,
            pkt["IP"].ttl,
            pkt["IP"].proto
        ])

def save():
    df = pd.DataFrame(features, columns=["pkt_len","ttl","proto"])
    df.to_csv("data/features.csv", index=False)
