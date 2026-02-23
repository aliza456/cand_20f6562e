import math
from collections import Counter

def entropy(y):
    if len(set(y)) == 1:
        return 0.0

    total = len(y)
    counts = Counter(y)
    ent = 0.0

    for cnt in counts.values():
        p = cnt / total
        ent -= p * math.log2(p)

    return round(ent, 4)
