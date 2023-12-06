from dataclasses import dataclass
from typing import List, Dict


paras = open('2023/day5/sample.txt').read().split('\n\n')
paras = open('2023/day5/data.txt').read().split('\n\n')

seeds, translations = paras[0], paras[1:]

seeds = [int(s) for s in seeds.removeprefix('seeds: ').split()]

current = [(a,a+b) for a,b in zip(seeds[::2], seeds[1::2])]

print(current)
print('-----')

for table in translations:

    # ================================= #
    # === Parse the table data ======== #

    rows = [tuple(map(int, row.split())) for row in table.split('\n')[1:]]
    i_start = [-99]
    offsets = [0]

    latest_end = -99
    # (dest_start, source_start, length) #
    for row in sorted(rows, key=lambda row: row[1]):
        if row[1] < latest_end:
            raise Exception('aaaaah')
        latest_end = max(latest_end, row[1]+row[2])

        offset = row[0] - row[1]
        if i_start and i_start[-1] == row[1]:
            i_start[-1] = row[1]
            offsets[-1] = offset
        else:
            i_start.append(row[1])
            offsets.append(offset)
        i_start.append(row[1]+row[2])
        offsets.append(0)

    debug = table == translations[2]
    debug = False
    if debug:
        print(i_start, offsets)
    
    # ================================= #
    # === Perform the Slicing ========= #


    out = []

    for interval in current:
        
        # tracking the boundaries
        splits = [interval[0]]

        # smash "current" through the grater
        start_index = None
        for idx, post in enumerate(i_start):
            if post <= splits[-1]:
                continue

            if start_index is None:
                start_index = idx - 1
            
            if post < interval[1]:
                if post != interval[1]:
                    splits.append(post)
            else:
                break
        
        splits.append(interval[1])

        start_index = start_index or len(offsets)

        if debug:
            print('intv', interval)
            print('splt', splits)
            print('sidx', start_index)

        for a,b in zip(splits, splits[1:]):
            dx = offsets[min(start_index or float('inf'), len(offsets)-1)]
            start_index += 1
            # print('dx', dx)

            out.append((a+dx, b+dx))
        
    current = out
    print(current)
    
print('min:', min(c[0] for c in current))
        




