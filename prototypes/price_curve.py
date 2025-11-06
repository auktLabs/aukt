"""price decay simulator."""

def price_curve(start, floor, steps):
    span = start - floor
    return [start - span * i / steps for i in range(steps + 1)]
