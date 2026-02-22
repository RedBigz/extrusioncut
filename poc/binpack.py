# https://web.archive.org/web/20240422115700/https://ics.uci.edu/~goodrich/teach/cs165/notes/BinPacking.pdf

"""
here, i'm going to implement a best-fit bin packing algorithm.

one important note about this algorithm is that it doesn't account for the varying bin (bar) sizes.
to correct this issue, i'll make the bars be selected in every permutation, over multiple passes.

obviously, this won't result in an optimal result, but i might add some substitution magic into this later.
"""

# TODO: substitution magic

# inputs
import itertools
import random


bars = [300, 360, 250]
cuts = [120, 140, 160, 180]

assert sum(cuts) <= sum(bars)

def binpack(b, c):
    bar_containers = [[] for _ in range(len(b))]
    available_bars = 1

    for cut in c:
        # sorry for the massive line! this sorts all the bars by how much length they have left and removes anything less than or equal to 0
        sortres = list(filter(lambda n: n[1] - sum(bar_containers[n[0]]) > 0, sorted(list(enumerate(b[:available_bars])), key=lambda ba: ba[1] - sum(bar_containers[ba[0]]), reverse=True)))
       
        bar_to_pack = sortres[0][0]
        bar_length = b[bar_to_pack]
        bar_container = bar_containers[bar_to_pack]
        bar_difference = bar_length - sum(bar_container)

        # print(sortres, cut, bar_to_pack, bar_length, bar_containers, bar_difference)

        if bar_difference < cut:
            available_bars += 1
            bar_containers[available_bars - 1].append(cut)
        else:
            bar_container.append(cut)

    return bar_containers

print("bars:", bars)
print("cuts:", cuts)

print()

print("trying all permutations of bars")

testlist = []

def test(b, c):
    try:
        testlist.append({"bars": b, "items": binpack(b, c)})
        return testlist[-1]
    except:
        return "errored"

for b in itertools.permutations(bars):
    print(test(b, sorted(cuts, reverse=True)))

best = sorted(testlist, key=lambda i: i["items"].count([]), reverse=True)

print()

print("best:", best[0])