

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

    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):

        # check if overlap
        if end > intervals[i].start: # overlapping
            end = intervals[i].end
        else: # not overlapping
            # save the last merge
            res.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    res.append(Interval(start, end))

    return res


def main():
    intervals = [Interval(1,4), Interval(3,4), Interval(6,10), Interval(7,12)]
    res = merge_intervals(intervals)

    for i in res:
        i.print_interval()


if __name__ == "__main__":
    main()
