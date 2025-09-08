from typing import List, Tuple


def identify_primer_pairs(sorted_hits: list[list[str]], max_amplicon_size: int) -> list[tuple[list[str], list[str]]]:
    primer_pairs = []
    for i, hit1 in enumerate(sorted_hits):
        for hit2 in sorted_hits[i:]:
            if hit1[1] == hit2[1]:
                start1, end1 = int(hit1[8]), int(hit1[9])
                start2, end2 = int(hit2[8]), int(hit2[9])

                # Determine amplification direction
                direction1 = 1 if start1 < end1 else -1
                direction2 = 1 if start2 < end2 else -1

                # Check if primers are pointing towards each other
                if direction1 != direction2:
                    # Find distance between 3' ends
                    distance = abs(end1 - end2)

                    if distance <= max_amplicon_size:
                        if end1 > end2:
                            hit1, hit2 = hit2, hit1
                        primer_pairs.append((hit1, hit2))

     # Sort primer pairs
    primer_pairs.sort(key=lambda x: int(x[0][8]))

    return primer_pairs

def step_two(sorted_hits: List[List[str]], max_amplicon_size: int) -> List[Tuple[List[str], List[str]]]:
    return identify_primer_pairs(sorted_hits, max_amplicon_size)


