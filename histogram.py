from __future__ import annotations
from collections import defaultdict
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from line_count import ModuleMeta

def log_buckets(initial_bucket_range: int, largest_needed: int):
    bucket_range = initial_bucket_range
    buckets: list[tuple[int, int]] = [(0, bucket_range)]
    while bucket_range+buckets[-1][1] < largest_needed:
        bucket_range *= 2
        buckets.append((buckets[-1][1]+1, buckets[-1][1]+bucket_range))
    return buckets

def modules_to_buckets(modules: list[ModuleMeta]) -> dict[str, int]:
    buckets = log_buckets(10, modules[-1].lines)
    bucketed = defaultdict(lambda: 0)
    for module in modules:
        for bucket in buckets:  # linear search with logarithmic complexity ???
            if bucket[0] <= module.lines <= bucket[1]:
                bucketed["-".join(map(str, bucket))] += 1
    return bucketed


if __name__ == "__main__":
    buckets = log_buckets(10, 257396)
    print(buckets)
    print([x[1]-x[0]+1 for x in buckets])
