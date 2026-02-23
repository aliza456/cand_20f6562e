import math

def top_k_cosine(query, docs, k):
    def cosine(q, d):
        dot = sum(qi * di for qi, di in zip(q, d))
        norm_q = math.sqrt(sum(qi * qi for qi in q))
        norm_d = math.sqrt(sum(di * di for di in d))
        if norm_q == 0 or norm_d == 0:
            return 0.0
        return dot / (norm_q * norm_d)

    sims = []
    for i, d in enumerate(docs):
        sims.append(( -cosine(query, d), i))  # negative for descending sort

    sims.sort()
    return [idx for _, idx in sims[:k]]
