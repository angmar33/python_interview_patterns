class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return (
            "[" + str(self.start) + ", " + str(self.end) + "]"
            if self.closed
            else "(" + str(self.start) + ", " + str(self.end) + ")"
        )


def merge_intervals(v: Interval) -> list:
    result: list = [Interval(v[0].start, v[0].end)]
    for i in range(1, len(v)):
        last_added = result[-1]
        if last_added.end >= v[i].start:
            last_added.end = max(result[-1].end, v[i].end)
        else:
            result.append(Interval(v[i].start, v[i].end))
    return result
