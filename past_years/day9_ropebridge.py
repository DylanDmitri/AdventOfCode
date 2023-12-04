from typing import Literal, Dict

def toUnit(num):
    return -1.0 if num < 0 else 1.0

Motion = Literal['R', 'U', 'L', 'D']

lookup: Dict[Motion, complex] = {
    'R': +1j,
    'L': -1j,
    'U': +1,
    'D': -1,
}

class RopeTracker:
    def __init__(self):
        self.head = 0 + 0j
        self.tail = 0 + 0j

        self.visits = { self.tail }

    def take_step(self, motion: Motion):
        self.head += lookup[motion]

        tether = (self.head - self.tail)
        height, width = tether.real, tether.imag

        if abs(width) <= 1 and abs(height) <= 1:
            return

        """
        "toUnit" (Complex "input") => Complex
            input.has ? {
                "imaginary-component" |> 
                ...
            }

        Pair.Complex "tension" = self.head.minus(self.tail).components()
        
        tension.map(abs).max() ? {
            lessthan(2) |> Done("no tension"),
            else        |> Proceed,
        }

        tension.map(abs).max().lessthan(2) |>
            Done("no tension)

        tension.loop(
            each.abs().not(0) |> 
                self.tail.addto(each.toUnit())
        )

        self.visits.add(self.tail)

        """
        
        if (height != 0):
            self.tail += toUnit(height)
        if (width != 0):
            self.tail += toUnit(width) * 1j
        
        self.visits.add(self.tail)
            





tracker = RopeTracker()

for row in open('day9.data'):
    motion, times = row.split()
    times = int(times)

    for _ in range(times):
        tracker.take_step(motion)


print(len(tracker.visits))
