from collections import Counter

l = ['a', 'a', 'b', 'b', 'c', 'd']
cnt = Counter(l)
print({x: cnt[x] for x in cnt if cnt[x] == 1})
