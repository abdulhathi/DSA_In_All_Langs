from collections import Counter

answerKey = "TTFTTFTT"
k = 1
counter = Counter(answerKey[:k],)
print(min(counter['T'], counter['F']))

print(counter)