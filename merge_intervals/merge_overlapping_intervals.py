

class Interval:
    def __init__(self, start, end):

        self.start = start
        self.end = end

    def print_interval(self):
        print(f'[{self.start}, {self.end}]')


def merge_intervals(intervals):

    # sort intervals depending on start
    intervals.sort(key=lambda x: x.start)
    res = []

    for i in range(len(intervals)):
        # compare to next and merge if necessary
        if i+1 < len(intervals):
            if intervals[i].end >= intervals[i+1].end: # overlapping region
                res.append(Interval(intervals[i].start,intervals[i+1].end))
                i = i + 1
            else:
                res.append(intervals[i])
        else:
            res.append(intervals[i])

    return res


def main():
    intervals = [Interval(1,4), Interval(3,4), Interval(6,7)]
    res = merge_intervals(intervals)

    for i in res:
        i.print_interval()


if __name__ == "__main__":
    main()
