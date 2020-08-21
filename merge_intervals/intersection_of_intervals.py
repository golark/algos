
class Interval:
    def __init__(self, start, end):

        self.start = start
        self.end = end

    def print_interval(self):
        print(f'[{self.start}, {self.end}]')


# intersection_of_intervals
# merge 2 intervals with only including the intersection between the intervals
# both lists are sorted with their start time
def intersection_of_intervals(l1, l2):

    i = 0
    j = 0
    start1 = l1[0].start
    end1 = l1[0].end
    start2 = l2[0].start
    end2 = l2[0].end
    res = []
    while i < len(l1) and j < len(l2):

        # detect overlap
        if max(start1, start2) < min(end1, end2):
            res.append(Interval(max(start1, start2), min(end1, end2)))

        if start1 > start2:
            j = j+1

            if j < len(l2):
                start2 = l2[j].start
                end2 = l2[j].end
        else:
            i = i+1

            if i < len(l1):
                start1 = l1[i].start
                end1 = l1[i].end

    return res


def main():

    l1 = [Interval(1,4), Interval(5,15),Interval(20, 30)]
    l2 = [Interval(5, 10), Interval(22, 26)]

    res = intersection_of_intervals(l1, l2)

    for i in res:
        i.print_interval()


if __name__ == "__main__":
    main()
