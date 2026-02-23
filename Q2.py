import math
from collections import Counter

def knn_predict(train_X, train_y, test_X, k):
    predictions = []

    for x in test_X:
        distances = []
        for xi, yi in zip(train_X, train_y):
            dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, xi)))
            distances.append((dist, yi))

        distances.sort()  # sorts by (distance, label)
        neighbors = distances[:k]

        counts = Counter(label for _, label in neighbors)
        max_count = max(counts.values())
        candidates = [label for label, cnt in counts.items() if cnt == max_count]

        predictions.append(min(candidates))

    return predictions
