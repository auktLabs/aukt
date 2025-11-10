"""price decay simulator."""

def price_curve(start, floor, steps):
    span = start - floor
    return [start - span * i / steps for i in range(steps + 1)]


def add_jitter(values, amp, rng):
    return [v + rng.uniform(-amp, amp) for v in values]
