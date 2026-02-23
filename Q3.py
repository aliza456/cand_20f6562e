def bow_transform(corpus, vocab):
    vocab_index = {word: i for i, word in enumerate(vocab)}
    result = []

    for doc in corpus:
        counts = [0] * len(vocab)
        for token in doc.split():
            if token in vocab_index:
                counts[vocab_index[token]] += 1
        result.append(counts)

    return result
