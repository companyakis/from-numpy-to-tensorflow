# https://www.w3schools.com/python/ref_set_update.asp

import numpy as np

sentences = np.array([
    "A barking dog never bites",
    "Out of sight, out of mind",
    "A rolling stone gathers no moss",
    "Mind means mind"
])

uniques = set()

for sentence in sentences:
  uniques.update(set(w.lower() for w in sentence.split()))

print(uniques)

"""

There should be 3 mind, but we see one... Python set...

{'never', 'moss', 'mind', 'dog', 'stone', 'no', 'barking', 'gathers', 'out', 'bites', 'of', 'means', 'rolling', 'a', 'sight,'}

"""
