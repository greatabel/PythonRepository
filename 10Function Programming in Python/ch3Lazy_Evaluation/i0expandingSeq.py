from collections.abc import Sequence

def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

class ExpandingSequence(Sequence):
    def __init__(self, it):
        self.it = it
        self._cache = []

    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]

    def __len__(self):
        return len(self._cache)

primes = ExpandingSequence(get_primes())
for _, p in zip(range(7), primes):
    print(p, end=" ")